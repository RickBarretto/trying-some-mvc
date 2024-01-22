from entities.clinic import Clinic

import tui
from tui import prompt

from menus.use_cases import current_session_manager, status
from menus.use_cases import patient_manager

def _should_create_new_patient(clinic: Clinic, cpf: str):
    return tui.progress(
        f"Deseja registrar paciente do CPF {cpf}?",
        patient_manager.register,
        clinic, patient_cpf=cpf
    )


def check_current_booking(clinic: Clinic) -> bool:
    """Verifica se paciente está agendado para a sessão atual.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Status do agendamento

    Warnings
    --------
    * Paciente não registrado

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`True`).
    """

    # Entrada do CPF
    try:
        cpf = prompt.get_cpf()
    except ValueError as e:
        tui.warn(e)
        return status.MayBeRepeated

    patient = clinic.patient_by_cpf(cpf)

    # Verifica se paciente existe no banco de dados

    if not patient:
        tui.warn("Paciente não registrado.")

        if _should_create_new_patient(clinic, cpf):
            patient = clinic.patient_by_cpf(cpf)
        else:
            return status.Ok

    # Verifica se paciente está marcado para a sessão atual
    is_booked = clinic.current_session.uid in patient.scheduled_sessions

    # Imprime o feedback

    TEMPLATE_MESSAGE = "Paciente {}{}está marcado para a sessão atual."
    message = TEMPLATE_MESSAGE.format(patient.name, " " if is_booked else " não ")

    tui.info(message)

    if not is_booked:
        if not tui.progress(
            "Desejas agendar paciente para a sessão atual?",
            patient_manager.book_schedule,
            clinic,
            patient=patient,
            session=clinic.current_session
        ):
            return status.Ok

    tui.progress(
        "Desejas por o paciente na fila de espera?",
        current_session_manager.send_to_waiting_queue,
        clinic,
        patient=patient,
    )
    return status.Ok
