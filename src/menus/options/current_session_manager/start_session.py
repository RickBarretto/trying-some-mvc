

from entities.clinic import ClinicController
from entities.session import SessionStatus
from screen.warning import WarningScreen


def start_current_session(clinic: ClinicController):
    """Inicia a sessão atual.

    Feedbacks
    ---------
    * Sessão inicializada

    Warnings
    --------
    * Sessão já inicializada
    * Sessão já finalizada
    """

    status = clinic.model.current_session.status

    # Verifica status da sessão
    if status == SessionStatus.BEGUN:
        WarningScreen("Sessão já foi iniciada.").render()
        return
    
    if status == SessionStatus.FINISHED:
        WarningScreen("Sessão já foi finalizada.").render()
        return

    # Ativa a sessão atual
    clinic.start_session()
    WarningScreen("Sessão iniciada!").render()