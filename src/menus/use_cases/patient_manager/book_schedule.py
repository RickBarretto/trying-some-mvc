import entities
from menus.use_cases import commons, propose, request, warnings
import tui


def book_schedule(
    clinic: entities.Clinic, patient: entities.Patient | None = None, session: entities.Session | None = None
):
    """Agenda uma sessão para um paciente.

    Questions
    ---------
    * CPF do paciente
    * Data da sessão

    Feedbacks
    ---------
    * Status do agendamento

    Warnings                        Proposes
    --------                        --------
    * Formato de data inválido
    * Formato de CPF inválido
    * Paciente não registrado       * Propõe registrar paciente
    * Sessão não registrada         * Propõe registrar sessão
    * Sessão já finalizada
    * Paciente já estava agendado

    """

    # ============= Verifica registro do paciente =============

    if not patient:
        patient = commons.get_patient(clinic)

    # ============= Verifica registro da sessão =============

    if not session:
        session_date = request.session_date()
        session = clinic.session_by_date(session_date)

    if not session:
        warnings.session_not_registered(session_date)
        if propose.register_session(clinic, session_date):
            return

        session = clinic.session_by_date(session_date)

    # ============= Agenda paciente + Feedback  =============

    if session.uid in patient.scheduled_sessions:
        warn_already_scheduled(patient, session)
        return
    
    _book_session(patient, session)


def _book_session(patient: entities.Patient, session: entities.Session):
    """Propriamente agenda paciente na sessão."""
    patient.scheduled_sessions.append(session.uid)
    tui.info(f"{patient.name} agendado para o dia {session.date}!")


def warn_already_scheduled(patient: entities.Patient, session: entities.Session):
    """Avisa que paciente já fora registrado."""
    message = (
        f"Paciente {patient.name} já está "
        f"registrado para a sessão {session.date}!"
    )
    tui.warn(message)