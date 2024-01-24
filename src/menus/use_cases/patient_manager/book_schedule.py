import entity
from menus.use_cases.commons import fetch
import tui


def book_schedule(
    clinic: entity.Clinic, patient: entity.Patient | None = None, session: entity.Session | None = None
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
        patient = fetch.patient_or_register(clinic)

    if not session:
        session = fetch.sesssion_or_register(clinic)

    # ============= Agenda paciente  =============

    if session.uid in patient.scheduled_sessions:
        warn_already_scheduled(patient, session)
        return
    
    _book_session(patient, session)


def _book_session(patient: entity.Patient, session: entity.Session):
    """Propriamente agenda paciente na sessão."""
    patient.scheduled_sessions.append(session.uid)
    tui.info(f"{patient.name} agendado para o dia {session.date}!")


def warn_already_scheduled(patient: entity.Patient, session: entity.Session):
    """Avisa que paciente já fora registrado."""
    message = (
        f"Paciente {patient.name} já está "
        f"registrado para a sessão {session.date}!"
    )
    tui.warn(message)