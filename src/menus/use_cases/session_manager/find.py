from entities.clinic import Clinic
from tui import prompt

import tui

from menus.use_cases import propose, request, status


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

    """

    # Valida entrada
    date = request.session_date()
    session = clinic.session_by_date(date)

    if session:
        tui.info([f"Sessão encontrada para o dia {date}.", f"Sessão: {session}"])
        return 

    tui.info(f"Sessão não encontrada para o dia {date}.")

    propose.register_session(clinic, date)
