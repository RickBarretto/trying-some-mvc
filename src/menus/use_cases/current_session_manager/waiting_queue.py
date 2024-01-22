from entities.clinic import Clinic
from entities.session import SessionStatus

from tui import prompt

import tui

from menus.use_cases import status


def send_to_waiting_queue(clinic: Clinic) -> bool:
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
    * Sessão não inicializada
    * Sessão já foi finalizada
    * Formato de CPF inválido
    * Paciente não registrado
    * Paciente já está na fila de espera

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Verifica status da sessão
    current_session_status = clinic.current_session.status

    # TODO: perguntar se deseja iniciar
    if current_session_status == SessionStatus.UNBEGUN:
        tui.warn("A sessão nunca foi inicializada.")
        return status.Ok

    if current_session_status == SessionStatus.FINISHED:
        tui.warn("A sessão ja foi finalizada.")
        return status.Ok

    # Valida a entrada do CPF
    try:
        cpf = prompt.get_cpf()
    except ValueError as e:
        tui.warn(e)
        return status.MayBeRepeated

    # Verifica se o paciente é registrado
    patient = clinic.patient_by_cpf(cpf)

    # TODO: perguntar se deseja registrar
    if not patient:
        tui.warn("Paciente não registrado.")
        return status.Ok

    # Verifica se o paciente já consta na fila de espera
    waiting_queue = clinic.waiting_queue
    if patient.uid in waiting_queue:
        tui.warn("Paciente já está na fila de espera.")
        return status.Ok

    # Põe o paciente na fila de espera
    clinic.waiting_queue.append(patient.uid)

    # Feedback

    tui.info([
        f"{patient.name} colocado na fila de espera,"
        f"O mesmo se encontra na posição {len(waiting_queue)}!"
    ])

    return status.Ok
