from entities.clinic import Clinic
from entities.session import Session, SessionStatus
from tui.warning import WarningScreen

from menus.use_cases import status


def update(clinic: Clinic, session: Session) -> bool:
    """Atualiza a sessão atual.

    Note
    ----
    Essa função em específica deve ser chamada pelo sistema em certas circunstâncias,
    e nunca pelo usuário.

    Feedbacks
    ---------
    * Sessão atual atualizada

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Atualiza a sessão atual
    clinic.current_session = session

    # TODO: Usar InfoScreen
    WarningScreen(f"Sessão atual atualizada para o dia {session.date}!").render()
    return status.Ok
