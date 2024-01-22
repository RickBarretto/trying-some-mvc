from entities.clinic import Clinic
from entities.session import SessionStatus

import tui

from menus.use_cases import status


def start(clinic: Clinic) -> bool:
    """Inicia a sessão atual.

    Feedbacks
    ---------
    * Sessão inicializada

    Warnings
    --------
    * Sessão já inicializada
    * Sessão já finalizada

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    session_status = clinic.current_session.status

    # Verifica status da sessão
    if session_status == SessionStatus.BEGUN:
        tui.warn("Sessão já foi iniciada.")
        return status.Ok

    if session_status == SessionStatus.FINISHED:
        tui.warn("Sessão já foi finalizada.")
        return status.Ok

    # Ativa a sessão atual
    clinic.current_session.status = SessionStatus.BEGUN

    # TODO: Usar InfoScreen
    tui.warn("Sessão iniciada!")
    return status.Ok
