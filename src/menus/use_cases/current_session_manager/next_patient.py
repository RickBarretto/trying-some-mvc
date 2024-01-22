from entities.clinic import Clinic
from entities.session import SessionStatus
import tui

from menus.use_cases import status
from menus.use_cases import proposes


def show_next_patient(clinic: Clinic) -> bool:
    """Mostra novo paciente

    Questions
    ---------
    * Nenhuma

    Feedbacks
    ---------
    * Informações básicas do paciente

    Warnings
    --------
    * Sessão nunca foi inicializada
    * Não há pacientes na fila

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`False`)
        ou `status.MayBeRepeated` (`True`).
    """
    waiting_queue = clinic.waiting_queue

    if clinic.current_session.status == SessionStatus.UNBEGUN:
        tui.warn("Sessão nunca foi iniciada!")
        if not proposes.wish_start_current_session(clinic):
            return status.Ok

    if clinic.current_session.status == SessionStatus.FINISHED:
        tui.warn("Sessão já foi finalizada!")
        return status.Ok

    # Verifica se a fila de espera está vazia

    if not waiting_queue:
        tui.warn("Não há pacientes na fila de espera.")
        return status.Ok

    # Pega a instância do próximo paciente
    next_patient_id = waiting_queue[0]
    patient = clinic.patient_by_id(next_patient_id)

    # Imprime informações do paciente
    content = ["Próximo paciente:", str(patient)]
    tui.info(content)
    return status.Ok
