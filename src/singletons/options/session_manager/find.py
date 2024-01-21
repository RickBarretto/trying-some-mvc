from entities.clinic import ClinicController
from screen.prompt import Prompt
from screen.warning import WarningScreen


def find_session(clinic: ClinicController):
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
    session = clinic.find_session(date)

    if session:
        WarningScreen(["Sessão encontrada.", session.formated_date, str(session.status)]).render()
    else:
        WarningScreen("Sessão não encontrada.").render()