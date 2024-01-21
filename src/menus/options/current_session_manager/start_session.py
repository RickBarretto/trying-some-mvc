

from entities.clinic import Clinic
from entities.session import SessionStatus
from tui.warning import WarningScreen


def start_current_session(clinic: Clinic):
    """Inicia a sessão atual.

    Feedbacks
    ---------
    * Sessão inicializada

    Warnings
    --------
    * Sessão já inicializada
    * Sessão já finalizada
    """

    status = clinic.current_session.status

    # Verifica status da sessão
    if status == SessionStatus.BEGUN:
        WarningScreen("Sessão já foi iniciada.").render()
        return
    
    if status == SessionStatus.FINISHED:
        WarningScreen("Sessão já foi finalizada.").render()
        return

    # Ativa a sessão atual
    clinic.current_session.status = SessionStatus.BEGUN
    WarningScreen("Sessão iniciada!").render()