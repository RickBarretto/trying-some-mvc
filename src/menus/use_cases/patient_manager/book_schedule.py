from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import Session
from tui import prompt

import tui

from menus.use_cases import status
from menus.use_cases import proposes
from menus.use_cases import session_manager
from menus.use_cases import patient_manager


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
    * Paciente não registrado
    * Sessão não registrada
    * Sessão já finalizada
    * Paciente já estava agendado

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Valida entradas
    try:
        if not patient:
            patient_cpf = prompt.get_cpf()
        if not session:
            session_date = prompt.get_date()
    except ValueError as e:
        tui.warn(e)
        return status.MayBeRepeated

    if not patient:
        patient = clinic.patient_by_cpf(patient_cpf)

    if not session:
        session = clinic.session_by_date(session_date)

    # Valida registros

    if not patient:
        tui.warn("Paciente não registrado.")

        if proposes.wish_register_patient(clinic, patient_cpf):
            patient = clinic.patient_by_cpf(patient_cpf)
        else:
            return status.Ok

    if not session:
        tui.warn("Sessão não registrada.")

        if proposes.wish_register_session(clinic, session_date):
            session = clinic.session_by_date(session_date)
        else:
            return status.Ok

    # Verifica o agendamento
    if session.uid in patient.scheduled_sessions:
        tui.warn(
            f"Paciente {patient.name} já está "
            f"registrado para a sessão {session.date}."
        )
        return status.Ok

    # Agenda sessão para paciente
    patient.scheduled_sessions.append(session.uid)

    tui.info(f"{patient.name} agendado para o dia {session.date}!")
    return status.Ok
