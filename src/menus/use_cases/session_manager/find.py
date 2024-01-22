from entities.clinic import Clinic
from menus.use_cases import session_manager
from tui import prompt

import tui

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
        date = prompt.get_date()
    except ValueError as e:
        tui.warn(e)
        return status.MayBeRepeated

    # Valida entrada
    session = clinic.session_by_date(date)

    if session:
        tui.info([f"Sessão encontrada para o dia {date}.", f"Sessão: {session}"])
    else:
        # TODO: pergunta se deseja registrar
        tui.info(f"Sessão não encontrada para o dia {date}.")
        if tui.progress(f"Deseja criar uma sessão no dia {date}?"):
            while session_manager.register(clinic, date=date) is status.MayBeRepeated:
                pass

    return status.Ok
