from entities.clinic import Clinic
import tui

from menus.use_cases import condition

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

    if not condition.has_active_current_session(clinic):
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

    if not condition.has_active_current_session(clinic):
        return

    # ============= Feedback =============

    if not clinic.waiting_queue:
        tui.warn("Não há pacientes na fila de espera.")
    else:
        _attend_next_patient(clinic)
        tui.info(["Paciente atual:", str(clinic.current_patient)])


def next_patient(clinic: Clinic) -> str:
    assert clinic.waiting_queue

    next_patient_id = clinic.waiting_queue[0]
    return str(clinic.patient_by_id(next_patient_id))


def _attend_next_patient(clinic: Clinic):
    patient_id = clinic.waiting_queue.pop(0)
    clinic.current_patient = clinic.patient_by_id(patient_id)
