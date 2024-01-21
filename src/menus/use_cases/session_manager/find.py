from entities.clinic import Clinic
from tui.prompt import Prompt
from tui.warning import WarningScreen

from menus.use_cases import status


def find(clinic: Clinic):
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

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Valida entrada
    try:
        date = Prompt.get_date()
    except ValueError as e:
        WarningScreen(e).render()
        return status.MayBeRepeated

    # Valida entrada
    session = clinic.session_by_date(date)

    if session:
        WarningScreen(["Sessão encontrada.", str(session)]).render()
    else:
        WarningScreen("Sessão não encontrada.").render()

    return status.Ok
