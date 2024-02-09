import entity
import tui
from menu.use_cases.commons import propose, request

__all__ = ["find"]


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

    session = _register_session(clinic, date)
    tui.info(f"Sessão registrada na data {date}")


def find(clinic: entity.Clinic):
    """Procura uma sessão no banco de dados.

    Questions
    ---------
    Data da sessão

    Feedbacks
    ---------
    Status da operação

    Warnings                        Proposes
    --------                        --------
    Formato de data inválido
    Sessão não registrada           Registrar sessão

    """

    # ============= Procura sessão =============

    date = request.session_date()
    session = clinic.session_by_date(date)

    # ============= Feedback =============

    if session:
        tui.info([f"Sessão encontrada para o dia {date}", f"Sessão: {session}"])
    else:
        tui.info(f"Sessão não encontrada para o dia {date}.")
        propose.register_session(clinic, date)


def list_all(clinic: entity.Clinic):
    """Lista todas as sessões registradas na clínica.

    Feedbacks
    ---------
    Lista de sessões
    Se há ou não alguma registrada

    """

    # ============= Lista sessões =============

    data = (
        [str(session) for session in clinic.sessions]
        if clinic.sessions
        else ["Não há sessões registradas."]
    )
    tui.bullet_list("Sessões registradas:", data)


# ============= Funções auxiliares =============


def _register_session(clinic: entity.Clinic, date: str) -> entity.Session:
    """Registra em ``clinic`` uma sessão na data ``date``"""
    new_id: int = clinic.new_session_id()
    session = entity.Session(uid=new_id, date=date)

    clinic.sessions.append(session)
    clinic.last_session_id = new_id
    return session
