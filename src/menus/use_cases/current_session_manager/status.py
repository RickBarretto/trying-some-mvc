import entities
from menus.use_cases import warnings
import tui


def start(clinic: entities.Clinic):
    """Inicia a sessão atual.

    Feedbacks
    ---------
    Sessão inicializada

    Warnings
    --------
    Sessão já inicializada
    Sessão já finalizada

    """

    # ============= Verifica status da sessão atual =============

    session_status = clinic.current_session.status
    has_already_begun = session_status == entities.SessionStatus.BEGUN
    has_been_finished = session_status == entities.SessionStatus.FINISHED

    if has_already_begun:
        warnings.session_has_already_started(clinic.current_session)
        return

    if has_been_finished:
        warnings.session_has_already_been_finished(clinic.current_session)
        return

    # ============= Ativa sessão atual =============

    _start_current_session(clinic)


def finish(clinic: entities.Clinic, suppress_warnings: bool = False):
    """Finaliza a sessão atual.

    Feedbacks
    ---------
    Sessão finalizada

    Warnings                        Propose
    --------                        -------
    Sessão nunca inicializada       Forçar finalização
    Sessão já finalizada

    """

    # ============= Verifica status da sessão atual =============

    session_status    = clinic.current_session.status
    has_not_begun     = session_status == entities.SessionStatus.UNBEGUN
    has_been_finished = session_status == entities.SessionStatus.FINISHED

    if not suppress_warnings:
        if has_not_begun:
            warnings.session_has_never_started(clinic.current_session)
            if not tui.proceed("Desejas finalizar mesmo assim?"):
                return
            
        if has_been_finished:
            warnings.session_has_already_been_finished(clinic.current_session)
            return

    # ============= Desativa sessão atual =============

    _finish_current_session(clinic)


def _start_current_session(clinic: entities.Clinic):
    clinic.current_session.status = entities.SessionStatus.BEGUN
    tui.info(f"Sessão {clinic.current_session.date} iniciada!")

def _finish_current_session(clinic: entities.Clinic):
    """Finaliza a sessão atual"""
    clinic.current_session.status = entities.SessionStatus.FINISHED
    tui.info(f"Sessão {clinic.current_session.date} finalizada!")
