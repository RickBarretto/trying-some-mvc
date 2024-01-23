from entities.clinic import Clinic
from entities.session import SessionStatus
from menus.use_cases import current_session_manager, session_manager, request

import tui


def update(clinic: Clinic):
    """Atualiza a sessão atual.

    Note
    ----
    Essa função em específica deve ser chamada pelo sistema em certas circunstâncias,
    e nunca pelo usuário.

    Feedbacks
    ---------
    * Sessão atual atualizada

    """

    # ============= Registra a sessão, caso necessário =============

    date = request.session_date()
    session_manager.register(clinic, date=date, suppress_warnings=True)
    session = clinic.session_by_date(date)

    # ============= Warnings =============

    if clinic.current_session == session:
        warn_returning_to_the_same_session()
        return

    if clinic.current_session:
        if clinic.current_session.status != SessionStatus.FINISHED:
            tui.warn(["A sessão atual não foi finalizada ainda!"])
            
            if not tui.progress("Desejas finalizá-la?"):
                warn_returning_to_the_same_session()
                return

            current_session_manager.finish(clinic, suppress_warnings=True)


    # ============= Atualiza sessão atual =============

    session = clinic.session_by_date(date)
    clinic.current_session = session

    # ============= Feedback =============

    tui.info(f"Sessão atual atualizada para o dia {session.date}!")


def warn_returning_to_the_same_session():
    tui.warn(["Retornando à mesma sessão atual!", "Sessão atual não atualizada!"])