from entities.clinic import ClinicController
from screen.prompt import Prompt
from screen.warning import WarningScreen


def register(clinic: ClinicController):
    """Registra uma nova sessão no banco de dados.

    Questions
    ---------
    * Data da sessão

    Feedbacks
    ---------
    * Status do registro

    Warnings
    --------
    * Formato de data inválido
    * Sessão já registrada
    """

    # Valida entrada
    try:
        date = Prompt.get_date()
    except ValueError as e:
        WarningScreen(e).render()
        return
    
    # Verifica registro
    session = clinic.find_session(date)
    if session:
        WarningScreen("Sessão já foi registrada.").render()
        return

    # Registra sessão
    session = clinic.register_session(date)
    WarningScreen(f"Sessão registrada na data {session.formated_date}.").render()