import entities
import tui
from menus.use_cases.commons import propose, request


def find(clinic: entities.Clinic):
    """Registra uma nova sessão no banco de dados.

    Questions
    ---------
    Data da sessão

    Feedbacks
    ---------
    Informações básicas da sessão

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
