from entities.clinic import ClinicController
from entities.session import SessionModel
from tui.prompt import Prompt
from tui.warning import WarningScreen


def register(clinic: ClinicController):
    """Registra uma nova sessão no banco de dados.

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
    if session:
        WarningScreen("Sessão já foi registrada.").render()
        return
    
    # Criação da sessão
    new_id: int = clinic.new_session_id
    session: SessionModel = SessionModel(uid=new_id, date=date)

    # Registro da nova sessão
    clinic.sessions.append(session)
    clinic.last_session_id = new_id

    # Registra sessão
    session = clinic.register_session(date)
    WarningScreen(f"Sessão registrada na data {session.formated_date}.").render()