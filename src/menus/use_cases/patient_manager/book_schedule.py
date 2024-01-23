from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import Session

from menus.use_cases import propose, request, warnings

import tui


def book_schedule(
    clinic: Clinic, patient: Patient | None = None, session: Session | None = None
):
    """Agenda uma sessão para um paciente.

    Questions
    ---------
    * CPF do paciente
    * Data da sessão

    Feedbacks
    ---------
    * Status do agendamento

    Warnings
    --------
    * Formato de data inválido
    * Formato de CPF inválido
    * Paciente não registrado   : Propõe o registrar
    * Sessão não registrada     : Propõe a registrar
    * Sessão já finalizada
    * Paciente já estava agendado

    """

    # ============= Verifica registro do paciente =============

    if not patient:
        patient_cpf = request.patient_cpf()
        patient = clinic.patient_by_cpf(patient_cpf)

    if not patient:
        warnings.patient_not_registered(patient_cpf)
        if not propose.register_patient(clinic, patient_cpf):
            return

        patient = clinic.patient_by_cpf(patient_cpf)

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
        message = (
            f"Paciente {patient.name} já está "
            f"registrado para a sessão {session.date}!"
        )
        tui.warn(message)
    else:
        patient.scheduled_sessions.append(session.uid)
        tui.info(f"{patient.name} agendado para o dia {session.date}!")
