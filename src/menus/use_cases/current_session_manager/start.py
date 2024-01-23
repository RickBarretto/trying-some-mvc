import entities
from menus.use_cases import warnings
import tui


def start(clinic: entities.Clinic):
    """Inicia a sessão atual.

    Feedbacks
    ---------
    * Sessão inicializada

    Warnings
    --------
    * Sessão já inicializada
    * Sessão já finalizada

    """

    # ============= Verifica status da sessão atual =============

    session_status = clinic.current_session.status

    if session_status == entities.SessionStatus.BEGUN:
        warnings.session_has_already_started(clinic.current_session)
        return

    if session_status == entities.SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return

    # ============= Ativa sessão atual =============

    clinic.current_session.status = entities.SessionStatus.BEGUN

    # ============= Feedback =============

    tui.info(f"Sessão {clinic.current_session.date} iniciada!")
