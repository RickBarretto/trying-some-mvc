from entities.clinic import Clinic
from tui import prompt

import tui

from menus.use_cases import proposes, request, status


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
    * Sessão não registrada     : Propõe a registrar

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`False`)
        ou `status.MayBeRepeated` (`True`).
    """

    # Valida entrada
    date = request.session_date()
    session = clinic.session_by_date(date)

    if session:
        tui.info([f"Sessão encontrada para o dia {date}.", f"Sessão: {session}"])
        return status.Ok

    tui.info(f"Sessão não encontrada para o dia {date}.")

    proposes.register_session(clinic, date)

    return status.Ok
