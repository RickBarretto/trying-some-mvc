from entities.clinic import Clinic
from entities.session import SessionStatus
import tui

from menus.use_cases import propose


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
    * Sessão nunca foi inicializada : Propõe a iniciar
    * Não há pacientes na fila

    """
    waiting_queue = clinic.waiting_queue

    if clinic.current_session.status == SessionStatus.UNBEGUN:
        tui.warn("Sessão nunca foi iniciada!")
        if not propose.start_current_session(clinic):
            return 

    if clinic.current_session.status == SessionStatus.FINISHED:
        tui.warn("Sessão já foi finalizada!")
        return 

    # Verifica se a fila de espera está vazia

    if not waiting_queue:
        tui.warn("Não há pacientes na fila de espera.")
        return 

    # Pega a instância do próximo paciente
    next_patient_id = waiting_queue[0]
    patient = clinic.patient_by_id(next_patient_id)

    # Imprime informações do paciente
    content = ["Próximo paciente:", str(patient)]
    tui.info(content)
