import entity
from app.use_cases.commons import condition, fetch, request
import tui

__all__ = [
    "annotate_medical_records",
    "book_schedule" "list_bookings",
    "list_all",
    "read_first_medical_annotation",
    "read_full_medical_records",
    "read_last_medical_annotation",
    "register",
]


def register(clinic: entity.Clinic, patient_cpf: str | None = None):
    """Registra paciente no banco de dados.

    Questions
    ---------
    CPF do paciente
    Nome do paciente
    Informações extras

    Feedbacks
    ---------
    Registro foi um sucesso

    Warnings
    --------
    Formato de CPF inválido
    Formato de nome inválido
    Paciente já registrado

    """

    # ============= Verifica registro de paciente =============

    if not patient_cpf:
        patient_cpf = request.patient_cpf()

    if clinic.patient_by_cpf(patient_cpf):
        tui.warn("Paciente já foi registrado!")
        return

    # ============= Adiciona dados extras =============

    patient_name: str = request.patient_name()
    extra_information: str = tui.multiline("Insira informações extra.")

    # ============= Registra paciente =============

    patient = _register_patient(clinic, patient_cpf, patient_name, extra_information)
    tui.info(f"{patient.name} registrado com sucesso!")


def list_bookings(clinic: entity.Clinic):
    """Lista os agendamentos de um paciente.

    Questions
    ---------
    CPF do paciente

    Feedbacks
    ---------
    Lista de agendamentos
    Nenhum agendamento

    Warnings                    Proposes
    --------                    --------
    Formato de CPF inválido
    Paciente não registrado     Registrar paciente

    """

    # ============= Verifica registro do paciente =============

    if not (patient := fetch.patient_or_register(clinic)):
        return

    # ============= Lista agendamentos =============

    tui.bullet_list(
        f"Sessões agendadas de {patient.name}:", _find_bookings(clinic, patient)
    )


def book_schedule(
    clinic: entity.Clinic,
    patient: entity.Patient | None = None,
    session: entity.Session | None = None,
):
    """Agenda uma sessão para um paciente.

    Questions
    ---------
    CPF do paciente
    Data da sessão

    Feedbacks
    ---------
    Status do agendamento

    Warnings                        Proposes
    --------                        --------
    Formato de data inválido
    Formato de CPF inválido
    Paciente não registrado         Registrar paciente
    Sessão não registrada           Registrar sessão
    Sessão já finalizada
    Paciente já estava agendado

    """

    # ============= Verifica registro do paciente e sessão =============

    if not patient:
        if not (patient := fetch.patient_or_register(clinic)):
            return

    if not session:
        if not (session := fetch.sesssion_or_register(clinic)):
            return

    # ============= Agenda paciente  =============

    if session.uid in patient.scheduled_sessions:
        _warn_already_scheduled(patient, session)
        return

    _book_session(patient, session)


def annotate_medical_records(clinic: entity.Clinic):
    """Faz anotação no prontuário do paciente atual.

    Questions
    ---------
    Anotação

    Feedbacks
    ---------
    Ação concluída

    Warnings                            Proposes
    --------                            --------
    Sessão atual não iniciada           Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    is_able_to_read = condition.has_patient_being_attended(
        clinic
    ) and condition.has_active_current_session_or_activate_it(clinic)

    if not is_able_to_read:
        return

    # ============= Anota no prontuário =============

    message = f"Anotar prontuário de {clinic.current_patient.name}:"
    annotation = tui.prompt(message)
    _save_annotation(clinic, annotation)

    # ============= Feedback =============

    tui.info("Anotação feita!")


def list_all(clinic: entity.Clinic):
    """Lista todos os pacientes registrados na clínica.

    Feedbacks
    ---------
    Lista de pacientes
    Se há ou não algum registrado
    """

    # ============= Lista sessões =============

    data = (
        [str(patient) for patient in clinic.patients]
        if clinic.sessions
        else ["Não há pacientes registrados."]
    )
    tui.bullet_list("Pacientes registrados:", data)


def read_full_medical_records(clinic: entity.Clinic):
    """Lê o prontuário médico completo do paciente atual.

    Feedbacks
    ---------
    Listagem das anotações
    Se há anotações

    Warnings                        Proposes
    --------                        --------
    Sessão atual não iniciada       Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    is_able_to_read = condition.has_patient_being_attended(
        clinic
    ) and condition.has_active_current_session_or_activate_it(clinic)

    if not is_able_to_read:
        return

    # ============= Feedback =============

    if not clinic.current_patient.medical_records:
        tui.info(f"{clinic.current_patient.name} não possui anotações médicas.")
        return

    tui.bullet_list(
        f"Prontuário médico de {clinic.current_patient.name}:",
        clinic.current_patient.medical_records,
        additional_margin=12,
    )


def read_first_medical_annotation(clinic: entity.Clinic):
    """Lê a primeira anotação do prontuário médico do paciente atual.

    Feedbacks
    ---------
    Primeira anotação
    Se não há anotações

    Warnings                        Proposes
    --------                        --------
    Sessão atual não iniciada       Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    is_able_to_read = condition.has_patient_being_attended(
        clinic
    ) and condition.has_active_current_session_or_activate_it(clinic)

    if not is_able_to_read:
        return

    # ============= Feedback =============

    if not clinic.current_patient.medical_records:
        tui.info(f"{clinic.current_patient.name} não possui anotações médicas.")
        return

    tui.info(
        [
            f"Primeira anotação médica de {clinic.current_patient.name}:",
            clinic.current_patient.medical_records[0],
        ]
    )


def read_last_medical_annotation(clinic: entity.Clinic):
    """Lê a primeira anotação do prontuário médico do paciente atual.

    Feedbacks
    ---------
    Primeira anotação
    Se não há anotações

    Warnings                        Proposes
    --------                        --------
    Sessão atual não iniciada       Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    is_able_to_read = condition.has_patient_being_attended(
        clinic
    ) and condition.has_active_current_session_or_activate_it(clinic)

    if not is_able_to_read:
        return

    # ============= Feedback =============

    if not clinic.current_patient.medical_records:
        tui.info(f"{clinic.current_patient.name} não possui anotações médicas.")
        return

    tui.info(
        [
            f"Última anotação médica de {clinic.current_patient.name}:",
            clinic.current_patient.medical_records[-1],
        ]
    )


def _book_session(patient: entity.Patient, session: entity.Session):
    """Propriamente agenda paciente na sessão."""
    patient.scheduled_sessions.append(session.uid)
    tui.info(f"{patient.name} agendado para o dia {session.date}!")


def _find_bookings(clinic: entity.Clinic, patient: entity.Patient) -> list[str]:
    sessions_ids = patient.scheduled_sessions
    sessions = [
        str(session) for session in clinic.sessions if session.uid in sessions_ids
    ]

    return sessions if sessions else ["Nenhuma sessão agendada"]


def _register_patient(
    clinic: entity.Clinic, cpf: str, name: str, extra: list[str]
) -> entity.Patient:
    new_id: int = clinic.new_patient_id()
    patient = entity.Patient(uid=new_id, cpf=cpf, name=name, extra_info=extra)

    clinic.patients.append(patient)
    clinic.last_patient_id_id = new_id

    return patient


def _save_annotation(clinic: entity.Clinic, note: str):
    """Formata e salva a anotação no prontuário."""
    formated_note = f"{clinic.current_session.date}: {note}"
    clinic.current_patient.medical_records.append(formated_note)


def _warn_already_scheduled(patient: entity.Patient, session: entity.Session):
    """Avisa que paciente já fora registrado."""
    message = (
        f"Paciente {patient.name} já está " f"registrado para a sessão {session.date}!"
    )
    tui.warn(message)
