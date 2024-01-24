import entities
from menus.use_cases import current_session_manager, session_manager, request
import tui


def update(clinic: entities.Clinic):
    """Atualiza a sessão atual.

    Note
    ----
    Essa função em específica deve ser chamada pelo sistema em certas circunstâncias,
    e nunca pelo usuário.

    Feedbacks
    ---------
    Sessão atual atualizada

    Warnings                        Proposes
    --------                        --------
    Retornando à mesma sessão
    Sessão não finalizada           Finalizar sessão atual

    """

    # ============= Registra a sessão, caso necessário =============

    date = request.session_date()
    session_manager.register(clinic, date=date, suppress_warnings=True)
    session = clinic.session_by_date(date)

    # ============= Warnings =============
    
    is_same_current_session = clinic.current_session == session

    if is_same_current_session:
        warn_returning_to_the_same_session()
        return

    if clinic.current_session:
        has_been_finished = clinic.current_session.status != entities.SessionStatus.FINISHED

        if has_been_finished:
            tui.warn(["A sessão atual não foi finalizada ainda!"])

            if not tui.proceed("Desejas finalizá-la?"):
                warn_returning_to_the_same_session()
                return

            current_session_manager.finish(clinic, suppress_warnings=True)

    # ============= Atualiza sessão atual =============
            
    _update_current_session_to_date(clinic, date)


def _update_current_session_to_date(clinic: entities.Clinic, date: str):
    session = clinic.session_by_date(date)
    clinic.current_session = session
    tui.info(f"Sessão atual atualizada para o dia {session.date}!")


def warn_returning_to_the_same_session():
    tui.warn(["Retornando à mesma sessão atual!", "Sessão atual não atualizada!"])
