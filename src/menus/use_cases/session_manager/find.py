from entities.clinic import Clinic
from tui import prompt

import tui

from menus.use_cases import status
from menus.use_cases import proposes


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
        Retorna o status da função, que pode ser `status.Ok` (`False`)
        ou `status.MayBeRepeated` (`True`).
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
        return status.Ok

    tui.info(f"Sessão não encontrada para o dia {date}.")

    proposes.wish_register_session(clinic, date)

    return status.Ok
