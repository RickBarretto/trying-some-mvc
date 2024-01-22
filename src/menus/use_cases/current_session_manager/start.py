from entities.clinic import Clinic
from entities.session import SessionStatus

import tui
from menus.use_cases import warnings


def start(clinic: Clinic) -> bool:
    """Inicia a sessão atual.

    Feedbacks
    ---------
    * Sessão inicializada

    Warnings
    --------
    * Sessão já inicializada
    * Sessão já finalizada
    
    """

    session_status = clinic.current_session.status

    # Verifica status da sessão
    if session_status == SessionStatus.BEGUN:
        warnings.session_has_already_started(clinic.current_session)
        return 

    if session_status == SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return 

    # Ativa a sessão atual
    clinic.current_session.status = SessionStatus.BEGUN

    tui.info("Sessão iniciada!")
