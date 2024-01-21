from entities.clinic import Clinic
from entities.session import SessionStatus

from tui.prompt import Prompt
from tui.warning import WarningScreen

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
        WarningScreen("A sessão nunca foi inicializada.").render()
        return status.Ok

    if current_session_status == SessionStatus.FINISHED:
        WarningScreen("A sessão ja foi finalizada.").render()
        return status.Ok

    # Valida a entrada do CPF
    try:
        cpf = Prompt.get_cpf()
    except ValueError as e:
        WarningScreen(e).render()
        return status.MayBeRepeated

    # Verifica se o paciente é registrado
    patient = clinic.patient_by_cpf(cpf)

    # TODO: perguntar se deseja registrar
    if not patient:
        WarningScreen("Paciente não registrado.").render()
        return status.Ok

    # Verifica se o paciente já consta na fila de espera
    waiting_queue = clinic.waiting_queue
    if patient.uid in waiting_queue:
        WarningScreen("Paciente já está na fila de espera.").render()
        return status.Ok

    # Põe o paciente na fila de espera
    clinic.waiting_queue.append(patient.uid)

    # Feedback

    # TODO: Usar InfoScreen
    WarningScreen(
        f"Paciente colocado na fila de espera na posição {len(waiting_queue)}!"
    ).render()

    return status.Ok
