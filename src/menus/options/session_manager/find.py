from entities.clinic import ClinicController
from tui.prompt import Prompt
from tui.warning import WarningScreen


def find(clinic: ClinicController):
    """Registra uma nova sessão no banco de dados.

    Questions
    ---------
    * Data da sessão

    Feedbacks
    ---------
    * Informações básicas da sessão

    Warnings
    --------
    * Formato de data inválido
    * Sessão não registrada
    """

    # Valida entrada
    try:
        date = Prompt.get_date()
    except ValueError as e:
        WarningScreen(e).render()
        return
    
    # Valida entrada
    session = clinic.session_by_date(date)

    if session:
        WarningScreen(["Sessão encontrada.", str(session)]).render()
    else:
        WarningScreen("Sessão não encontrada.").render()