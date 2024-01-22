from entities.clinic import Clinic
from entities.session import Session
from menus.use_cases import current_session_manager, status
from tui import prompt

import tui


def register(
    clinic: Clinic, dry_run: bool = False, should_update: bool = False,
    date: str | None = None
) -> bool:
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

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Valida entrada
    try:
        if date is None:
            date = prompt.get_date()
    except ValueError as e:
        tui.warn(e)
        return status.MayBeRepeated

    # Verifica registro
    session = clinic.session_by_date(date)

    if session and dry_run:
        tui.info("Entrando na sessão novamente.")
        return status.Ok

    if session:
        tui.warn("Sessão já foi registrada.")
        return status.Ok

    # Criação da sessão
    new_id: int = clinic.new_session_id()
    session: Session = Session(uid=new_id, date=date)

    # Registro da nova sessão
    clinic.sessions.append(session)
    clinic.last_session_id = new_id

    tui.info(f"Sessão registrada na data {session.date}.")

    # Atualiza a sessão caso a função seja chamada por fora
    if should_update:
        current_session_manager.update(clinic, session)

    return status.Ok
