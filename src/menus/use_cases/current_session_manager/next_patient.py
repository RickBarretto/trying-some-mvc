from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import SessionStatus
import tui

from menus.use_cases import propose, warnings


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

    if clinic.current_session.status == SessionStatus.UNBEGUN:
        warnings.session_has_never_started(clinic.current_session)
        if not propose.start_current_session(clinic):
            return

    if clinic.current_session.status == SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return

    # ============= Feedback =============

    if not clinic.waiting_queue:
        tui.warn("Não há pacientes na fila de espera.")
    else:
        tui.info(["Próximo paciente:", next_patient(clinic)])


def next_patient(clinic: Clinic) -> str:
    assert clinic.waiting_queue

    next_patient_id = clinic.waiting_queue[0]
    return str(clinic.patient_by_id(next_patient_id))
