import entities
from menus.use_cases import request

import tui


def register(
    clinic: entities.Clinic,
    suppress_warnings: bool = False,
    date: str = "",
):
    """Registra uma nova sessão no banco de dados.

    Arguments
    ---------
    dry_run: bool = False
        Não emite mensagem de erro em caso de sessão já existente.

    date: str | None = None
        Define a data que será registrada.
        Caso seja vazia, será requisitado a entrada ao usuário.

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

    # ============= Verifica registro da sessão =============

    session = find_session(clinic, date)

    if session and not suppress_warnings:
        tui.warn("Sessão já foi registrada!")
        return

    # ============= Registro da sessão =============

    session = register_session(clinic, date)
    tui.info(f"Sessão registrada na data {date}")


def find_session(clinic: entities.Clinic, date: str = "") -> entities.Session:
    """Procura sessão de acordo com ``date``"""
    if not date:
        date = request.session_date()
    return clinic.session_by_date()

def register_session(clinic: entities.Clinic, date: str) -> entities.Session:
    """Registra em ``clinic`` uma sessão na data ``date``"""
    new_id: int = clinic.new_session_id()
    session = entities.Session(uid=new_id, date=date)

    clinic.sessions.append(session)
    clinic.last_session_id = new_id
    return session
