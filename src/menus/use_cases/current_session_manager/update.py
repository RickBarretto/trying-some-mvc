from entities.clinic import Clinic
from entities.session import Session, SessionStatus
from tui.warning import WarningScreen


def update(clinic: Clinic, session: Session):
    """Atualiza a sessão atual.

    Note
    ----
    Essa função em específica deve ser chamada pelo sistema em certas circunstâncias,
    e nunca pelo usuário.

    Feedbacks
    ---------
    * Sessão atual atualizada
    """

    # Atualiza a sessão atual
    clinic.current_session = session
    WarningScreen(f"Sessão atual atualizada para o dia {session.date}!").render()
