import entities
from menus.use_cases import warnings
import tui


def finish(clinic: entities.Clinic, suppress_warnings: bool = False):
    """Finaliza a sessão atual.

    Feedbacks
    ---------
    * Sessão finalizada

    Warnings
    --------
    * Sessão já inicializada
    * Sessão já finalizada

    """

    # ============= Verifica status da sessão atual =============

    session_status = clinic.current_session.status

    if not suppress_warnings:
    
        has_not_begun     = session_status == entities.SessionStatus.UNBEGUN
        has_been_finished = session_status == entities.SessionStatus.FINISHED
        
        if has_not_begun:
            warnings.session_has_never_started(clinic.current_session)
            if not tui.proceed("Desejas finalizar mesmo assim?"):
                return
            
        if has_been_finished:
            warnings.session_has_already_been_finished(clinic.current_session)
            return

    # ============= Desativa sessão atual =============

    _finish_current_session(clinic)


def _finish_current_session(clinic: entities.Clinic):
    """Finaliza a sessão atual"""
    clinic.current_session.status = entities.SessionStatus.FINISHED
    tui.info(f"Sessão {clinic.current_session.date} finalizada!")
