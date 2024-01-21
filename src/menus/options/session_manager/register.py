from entities.clinic import ClinicModel
from entities.session import Session
from menus.options import current_session_manager
from tui.prompt import Prompt
from tui.warning import WarningScreen


def register(clinic: ClinicModel, dry_run: bool = False, should_update: bool = False) -> bool | None:
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

    # Valida entrada
    try:
        date = Prompt.get_date()
    except ValueError as e:
        WarningScreen(e).render()
        return
    
    # Verifica registro
    session = clinic.session_by_date(date)

    if session and dry_run:
        WarningScreen("Entrando na sessão novamente.").render()
        return True

    if session:
        WarningScreen("Sessão já foi registrada.").render()
        return
    
    # Criação da sessão
    new_id: int = clinic.new_session_id()
    session: Session = Session(uid=new_id, date=date)

    # Registro da nova sessão
    clinic.sessions.append(session)
    clinic.last_session_id = new_id

    WarningScreen(f"Sessão registrada na data {session.formated_date}.").render()

    # Atualiza a sessão caso a função seja chamada por fora
    if should_update:
        current_session_manager.update(clinic, session)

    return True