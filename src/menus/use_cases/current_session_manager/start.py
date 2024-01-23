from entities.clinic import Clinic
from entities.session import SessionStatus

import tui
from menus.use_cases import warnings


def start(clinic: Clinic):
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

    if session_status == SessionStatus.BEGUN:
        warnings.session_has_already_started(clinic.current_session)
        return

    if session_status == SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return

    # ============= Ativa sessão atual =============

    clinic.current_session.status = SessionStatus.BEGUN

    # ============= Feedback =============

    tui.info("Sessão iniciada!")
