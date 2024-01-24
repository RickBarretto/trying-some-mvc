import entities
import tui
from menus.use_cases import commons, propose, warnings


def send_to_waiting_queue(
    clinic: entities.Clinic, patient: entities.Patient | None = None
):
    """Envia um paciente para a fila de espera.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Paciente posto na fila de espera
    * Posição na fila de espera

    Warnings
    --------
    * Sessão não inicializada   : Propõe a inicializar
    * Sessão já foi finalizada
    * Formato de CPF inválido
    * Paciente não registrado   : Propõe o registrar
    * Paciente não agendado     : Propõe o agendar para a sessão atual
    * Paciente já está na fila de espera

    """

    # ============= Verifica status da sessão atual =============

    if session_has_never_begun(clinic.current_session):
        if not propose.start_current_session(clinic):
            return

    if session_has_already_finished(clinic.current_session):
        return

    # ============= Pega input do usuário =============

    if not patient:
        patient = commons.get_patient(clinic)

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


def _send_patient_to_queue(clinic: entities.Clinic, patient: entities.Patien):
    clinic.waiting_queue.append(patient.uid)
    
    message = [
        f"{patient.name} colocado na fila de espera",
        f"O mesmo se encontra na posição {len(clinic.waiting_queue)}.",
    ]

    tui.info(message)


def session_has_already_finished(session: entities.Session):
    if res := (session.status == entities.SessionStatus.FINISHED):
        warnings.session_has_already_been_finished(session)

    return res


def session_has_never_begun(session: entities.Session) -> bool:
    if res := (session.status == entities.SessionStatus.UNBEGUN):
        warnings.session_has_never_started(session)

    return res
