from entities.clinic import Clinic
from entities.session import SessionStatus
import tui

from menus.use_cases import propose, warnings

__all__ = ["attend_next_patient", "show_next_patient"]


def show_next_patient(clinic: Clinic):
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

    # ============= Verificação do status da sessão atual =============

    if not has_valid_status(clinic):
        return

    # ============= Feedback =============

    if not clinic.waiting_queue:
        tui.warn("Não há pacientes na fila de espera.")
    else:
        tui.info(["Próximo paciente:", next_patient(clinic)])


def attend_next_patient(clinic: Clinic):
    """Atende o próximo paciente da fila de espera.

    Feedbacks
    ---------
    * Fila de espera vazia
    * Novo paciente chamado

    """

    # ============= Verificação do status da sessão atual =============

    if not has_valid_status(clinic):
        return

    # ============= Feedback =============

    if not clinic.waiting_queue:
        tui.warn("Não há pacientes na fila de espera.")
    else:
        attend_next_patient(clinic)
        tui.info(["Paciente atual:", clinic.current_patient])


def has_valid_status(clinic: Clinic) -> bool:
    if clinic.current_session.status == SessionStatus.UNBEGUN:
        warnings.session_has_never_started(clinic.current_session)
        if not propose.start_current_session(clinic):
            return False

    if clinic.current_session.status == SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return False
    
    return True

def next_patient(clinic: Clinic) -> str:
    assert clinic.waiting_queue

    next_patient_id = clinic.waiting_queue[0]
    return str(clinic.patient_by_id(next_patient_id))
    

def attend_next_patient(clinic: Clinic):
    patient_id = clinic.waiting_queue.pop(0)
    clinic.current_patient = clinic.patient_by_id(patient_id)