from entities.clinic import Clinic
from entities.session import Session
from menus.use_cases import current_session_manager, request

import tui


def register(
    clinic: Clinic,
    dry_run: bool = False,
    should_update: bool = False,
    date: str | None = None,
):
    """Registra uma nova sessão no banco de dados.

    Arguments
    ---------
    dry_run: bool = False
        Não emite mensagem de erro em caso de sessão já existente.

    should_update: bool = False
        Define se a função deve atualizar a sessão atual.

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

    if not date:
        date = request.session_date()

    session = clinic.session_by_date(date)

    if session and dry_run:
        tui.info("Entrando na sessão novamente.")
        return

    if session:
        tui.warn("Sessão já foi registrada.")
        return

    # ============= Registro da sessão =============

    session = register_session(clinic, date)
    tui.info(f"Sessão registrada na data {session.date}.")

    # ============= Atualiza sessão atual =============

    if should_update:
        current_session_manager.update(clinic, session)


def register_session(clinic: Clinic, date: str) -> Session:
    new_id: int = clinic.new_session_id()
    session: Session = Session(uid=new_id, date=date)

    clinic.sessions.append(session)
    clinic.last_session_id = new_id
    return session
