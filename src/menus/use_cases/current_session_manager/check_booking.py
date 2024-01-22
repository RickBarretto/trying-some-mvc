from entities.clinic import Clinic

import tui
from tui import prompt

from menus.use_cases import status
from menus.use_cases import proposes


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

        if proposes.register_patient(clinic, cpf):
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
        if not proposes.book_session(clinic, patient, clinic.current_session):
            return status.Ok

    proposes.send_patient_to_waiting_queue(clinic, patient)
    return status.Ok
