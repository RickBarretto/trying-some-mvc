from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import Session

from menus.use_cases import propose, request, warnings

import tui


def book_schedule(
    clinic: Clinic, patient: Patient | None = None, session: Session | None = None
) -> bool:
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

    # Valida entradas

    if not patient:
        patient_cpf = request.patient_cpf()
        patient = clinic.patient_by_cpf(patient_cpf)

    if not session:
        session_date = request.session_date()
        session = clinic.session_by_date(session_date)

    # Valida registros

    # TODO: Improve menu with faster feedback

    if not patient:
        warnings.patient_not_registered(patient_cpf)
        if propose.register_patient(clinic, patient_cpf):
            patient = clinic.patient_by_cpf(patient_cpf)
        else:
            return 

    if not session:
        warnings.session_not_registered(session_date)

        if propose.register_session(clinic, session_date):
            session = clinic.session_by_date(session_date)
        else:
            return 

    # Verifica o agendamento
    if session.uid in patient.scheduled_sessions:
        tui.warn(
            f"Paciente {patient.name} já está "
            f"registrado para a sessão {session.date}."
        )
        return 

    # Agenda sessão para paciente
    patient.scheduled_sessions.append(session.uid)

    tui.info(f"{patient.name} agendado para o dia {session.date}!")
