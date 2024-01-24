import entities
from menus.use_cases.commons import condition
import tui

__all__ = ["attend_next_patient", "show_next_patient"]


def show_next_patient(clinic: entities.Clinic):
    """Mostra novo paciente

    Questions
    ---------
    Nenhuma

    Feedbacks
    ---------
    Informações básicas do paciente

    Warnings                        Propose
    --------                        -------
    Sessão nunca foi inicializada   Iniciar sessão atual
    Sessão finalizada
    Não há pacientes na fila

    """

    # ============= Verificação do status da sessão atual =============

    if not condition.has_active_current_session_or_activate_it(clinic):
        return

    # ============= Feedback =============

    if not clinic.waiting_queue:
        _warn_empty_queue()
        return
        
    _show_next_patient(clinic)


def attend_next_patient(clinic: entities.Clinic):
    """Atende o próximo paciente da fila de espera.

    Feedbacks
    ---------
    Fila de espera vazia
    Novo paciente chamado

    Warnings                Proposes
    --------                --------    
    Sessão não iniciada     Iniciar sessão
    Sessão já finalizada

    """

    # ============= Verificação do status da sessão atual =============

    if not condition.has_active_current_session_or_activate_it(clinic):
        return

    # ============= Verifica a fila de espera =============

    if not clinic.waiting_queue:
        _warn_empty_queue()
        return
    
    # ============= Atende próximo paciente =============
    
    _attend_next_patient(clinic)

def _warn_empty_queue():
        tui.warn("Não há pacientes na fila de espera.")

def _show_next_patient(clinic: entities.Clinic) -> entities.Patient:
    """Retorna o próximo paciente
    
    Assertions
    ----------
    ``clinic.waiting_queue`` tem pacientes
    """
    assert clinic.waiting_queue

    next_patient_id = clinic.waiting_queue[0]
    patient = clinic.patient_by_id(next_patient_id)
    tui.info(["Próximo paciente:", str(patient)])


def _attend_next_patient(clinic: entities.Clinic):
    """Atende próximo paciente
    
    Coloca o primeiro paciente da fila como paciente atual.
    """
    patient_id = clinic.waiting_queue.pop(0)
    clinic.current_patient = clinic.patient_by_id(patient_id)
    tui.info(["Paciente atual:", str(clinic.current_patient)])
