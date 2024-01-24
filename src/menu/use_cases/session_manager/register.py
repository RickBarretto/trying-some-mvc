import entity
from menu.use_cases import current_session_manager
from menu.use_cases.commons import request
import tui


def register(clinic: entity.Clinic, date: str = ""):
    """Registra uma nova sessão no banco de dados.

    Questions
    ---------
    Data da sessão

    Feedbacks
    ---------
    Status do registro

    Warnings
    --------
    Formato de data inválido
    Sessão já registrada

    """

    # ============= Verifica registro da sessão =============

    if not date:
        date = request.session_date()

    session = clinic.session_by_date(date)

    if session:
        tui.warn("Sessão já foi registrada!")
        return

    # ============= Registro da sessão =============

    session = register_session(clinic, date)
    tui.info(f"Sessão registrada na data {date}")


def register_session(clinic: entity.Clinic, date: str) -> entity.Session:
    """Registra em ``clinic`` uma sessão na data ``date``"""
    new_id: int = clinic.new_session_id()
    session = entity.Session(uid=new_id, date=date)

    clinic.sessions.append(session)
    clinic.last_session_id = new_id
    return session
