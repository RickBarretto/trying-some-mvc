import entity
import tui
from menu.use_cases.commons import propose, request

__all__ = ["find"]


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
