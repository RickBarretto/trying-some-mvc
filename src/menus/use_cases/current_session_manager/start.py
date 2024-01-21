from entities.clinic import Clinic
from entities.session import SessionStatus
from tui.warning import WarningScreen

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
        WarningScreen("Sessão já foi iniciada.").render()
        return status.Ok

    if session_status == SessionStatus.FINISHED:
        WarningScreen("Sessão já foi finalizada.").render()
        return status.Ok

    # Ativa a sessão atual
    clinic.current_session.status = SessionStatus.BEGUN
    WarningScreen("Sessão iniciada!").render()
    return status.Ok
