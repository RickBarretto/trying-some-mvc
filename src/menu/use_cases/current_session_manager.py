import entity
from menu.use_cases import session_manager
from menu.use_cases.commons import condition, fetch, propose, request, warnings
import tui

__all__ = [
    "attend_next_patient",
    "check_current_booking",
    "finish",
    "send_to_waiting_queue",
    "show_next_patient",
    "start",
    "update",
]

def start(clinic: entity.Clinic):
    """Inicia a sessão atual.

    Feedbacks
    ---------
    Sessão inicializada

    Warnings
    --------
    Sessão já inicializada
    Sessão já finalizada

    """

    # ============= Verifica status da sessão atual =============

    session_status = clinic.current_session.status
    has_already_begun = session_status == entity.SessionStatus.BEGUN
    has_been_finished = session_status == entity.SessionStatus.FINISHED

    if has_already_begun:
        warnings.session_has_already_started(clinic.current_session)
        return

    if has_been_finished:
        warnings.session_has_already_been_finished(clinic.current_session)
        return

    # ============= Ativa sessão atual =============

    _start_current_session(clinic)

def update(clinic: entity.Clinic, first_time: bool = False):
    """Atualiza a sessão atual.

    Note
    ----
    Essa função em específica deve ser chamada pelo sistema em certas circunstâncias,
    e nunca pelo usuário.

    Feedbacks
    ---------
    Sessão atual atualizada

    Warnings                        Proposes
    --------                        --------
    Retornando à mesma sessão
    Sessão atual não finalizada     Forçar finalização

    """

    # ============= Registra a sessão, caso necessário =============

    date = request.session_date()
    session = clinic.session_by_date(date)

    # ============= Warnings =============

    is_same_current_session = clinic.current_session == session

    if is_same_current_session and not first_time:
        _warn_returning_to_the_same_session()
        return

    if clinic.current_session and not first_time:
        has_been_finished = (
            clinic.current_session.status != entity.SessionStatus.FINISHED
        )

        if has_been_finished:
            tui.warn(["A sessão atual não foi finalizada ainda!"])

            if not tui.proceed("Desejas finalizá-la?"):
                _warn_returning_to_the_same_session()
                return

            finish(clinic, suppress_warnings=True)

    # ============= Atualiza sessão atual =============

    if not session:
        session_manager.register(clinic, date=date)

    _update_current_session_to_date(clinic, date)

def finish(clinic: entity.Clinic, suppress_warnings: bool = False):
    """Finaliza a sessão atual.

    Feedbacks
    ---------
    Sessão finalizada

    Warnings                        Propose
    --------                        -------
    Sessão nunca inicializada       Forçar finalização
    Sessão já finalizada

    """

    # ============= Verifica status da sessão atual =============

    session_status = clinic.current_session.status
    has_not_begun = session_status == entity.SessionStatus.UNBEGUN
    has_been_finished = session_status == entity.SessionStatus.FINISHED

    if not suppress_warnings:
        if has_not_begun:
            warnings.session_has_never_started(clinic.current_session)
            if not tui.proceed("Desejas finalizar mesmo assim?"):
                return

        if has_been_finished:
            warnings.session_has_already_been_finished(clinic.current_session)
            return

    # ============= Desativa sessão atual =============

    _finish_current_session(clinic)


def show_next_patient(clinic: entity.Clinic):
    """Mostra novo paciente

    Questions
    ---------
    Nenhuma

    Feedbacks
    ---------
    Informações básicas do paciente

    Warnings                        Propose
    --------                        -------
    Sessão nunca foi inicializada   Iniciar sessão atual
    Sessão finalizada
    Não há pacientes na fila

    """

    # ============= Verificação do status da sessão atual =============

    if not condition.has_active_current_session_or_activate_it(clinic):
        return

    # ============= Feedback =============

    if not clinic.waiting_queue:
        _warn_empty_queue()
        return

    _show_next_patient(clinic)


def attend_next_patient(clinic: entity.Clinic):
    """Atende o próximo paciente da fila de espera.

    Feedbacks
    ---------
    Fila de espera vazia
    Novo paciente chamado

    Warnings                Proposes
    --------                --------
    Sessão não iniciada     Iniciar sessão
    Sessão já finalizada

    """

    # ============= Verificação do status da sessão atual =============

    if not condition.has_active_current_session_or_activate_it(clinic):
        return

    # ============= Verifica a fila de espera =============

    if not clinic.waiting_queue:
        _warn_empty_queue()
        clinic.current_patient = None
        return

    # ============= Atende próximo paciente =============

    _attend_next_patient(clinic)



def send_to_waiting_queue(clinic: entity.Clinic, patient: entity.Patient | None = None):
    """Envia um paciente para a fila de espera.

    Questions
    ---------
    CPF do paciente

    Feedbacks
    ---------
    Paciente posto na fila de espera
    Posição na fila de espera

    Warnings                                Proposes
    --------                                --------
    Sessão não inicializada                 Iniciar sessão atual
    Sessão já foi finalizada
    CPF inválido
    Paciente não registrado                 Registrar paciente
    Paciente não agendado                   Agendar paciente para a sessão atual
    Paciente já está na fila de espera

    """

    # ============= Verifica status da sessão atual =============

    if not condition.has_active_current_session_or_activate_it(clinic):
        return

    # ============= Pega input do usuário =============

    if not patient:
        if not (patient := fetch.patient_or_register(clinic)):
            return

    # ============= Verifica agendamento do paciente =============

    if clinic.current_session.uid not in patient.scheduled_sessions:
        tui.warn(f"{patient.name} não está agendado para a sessão atual!")
        if not propose.book_session(clinic, patient, clinic.current_session):
            return

    # ============= Verifica se paciente está na fila =============

    if patient.uid in clinic.waiting_queue:
        tui.warn("Paciente já está na fila de espera!")
        return

    # ============= Põe paciente na fila =============
    _send_patient_to_queue(clinic, patient)


def check_current_booking(clinic: entity.Clinic):
    """Verifica se paciente está agendado para a sessão atual.

    Questions
    ---------
    CPF do paciente

    Feedbacks
    ---------
    Status do agendamento

    Warnings                    Proposes
    --------                    --------
    CPF inválido
    Paciente não registrado     Registrar paciente
    [ok]                        Agendar sessão
    [ok]                        Enviar paciente para fila de espera

    """

    # ============= Verificação do paciente no banco de dados =============

    if not (patient := fetch.patient_or_register(clinic)):
        return

    # ============= Verificação do agendamento =============

    is_booked = clinic.current_session.uid in patient.scheduled_sessions
    _show_checking_feedback(patient, is_booked)

    # ============= Proposta de agendamento =============

    if not is_booked:
        if not propose.book_session(clinic, patient, clinic.current_session):
            return

    # ============= Proposta de enfileiramento do paciente =============

    propose.send_patient_to_waiting_queue(clinic, patient)


# ============= Funções auxiliares =============

def _attend_next_patient(clinic: entity.Clinic):
    """Atende próximo paciente

    Coloca o primeiro paciente da fila como paciente atual.
    """
    patient_id = clinic.waiting_queue.pop(0)
    clinic.current_patient = clinic.patient_by_id(patient_id)
    tui.info(["Paciente atual:", str(clinic.current_patient)])


def _show_checking_feedback(patient: entity.Patient, is_booked: bool):
    message_start = patient.name + " " + ("" if is_booked else "não")
    message_end = "está marcado para a sessão atual"

    tui.info(f"{message_start} {message_end}")

def _warn_empty_queue():
    tui.warn("Não há pacientes na fila de espera.")


def _show_next_patient(clinic: entity.Clinic) -> entity.Patient:
    """Retorna o próximo paciente

    Assertions
    ----------
    ``clinic.waiting_queue`` tem pacientes
    """
    assert clinic.waiting_queue

    next_patient_id = clinic.waiting_queue[0]
    patient = clinic.patient_by_id(next_patient_id)
    tui.info(["Próximo paciente:", str(patient)])

def _start_current_session(clinic: entity.Clinic):
    clinic.current_session.status = entity.SessionStatus.BEGUN
    tui.info(f"Sessão {clinic.current_session.date} iniciada!")


def _finish_current_session(clinic: entity.Clinic):
    """Finaliza a sessão atual"""
    clinic.current_session.status = entity.SessionStatus.FINISHED
    tui.info(f"Sessão {clinic.current_session.date} finalizada!")

def _update_current_session_to_date(clinic: entity.Clinic, date: str):
    session = clinic.session_by_date(date)
    clinic.current_session = session
    tui.info(f"Sessão atual atualizada para o dia {session.date}!")


def _warn_returning_to_the_same_session():
    tui.warn(["Retornando à mesma sessão!", "Operação cancelada!"])

def _send_patient_to_queue(clinic: entity.Clinic, patient: entity.Patient):
    clinic.waiting_queue.append(patient.uid)

    message = [
        f"{patient.name} colocado na fila de espera",
        f"O mesmo se encontra na posição {len(clinic.waiting_queue)}.",
    ]

    tui.info(message)