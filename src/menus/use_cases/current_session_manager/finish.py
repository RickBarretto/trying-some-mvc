from entities.clinic import Clinic
from entities.session import SessionStatus

import tui
from menus.use_cases import condition, warnings


def finish(clinic: Clinic, suppress_warnings: bool = False):
    """Finaliza a sessão atual.

    Feedbacks
    ---------
    * Sessão finalizada

    Warnings
    --------
    * Sessão já inicializada
    * Sessão já finalizada

    """

    # ============= Verifica status da sessão atual =============

    session_status = clinic.current_session.status

    if not suppress_warnings:
        if session_status == SessionStatus.UNBEGUN:
            warnings.session_has_never_started(clinic.current_session)
            if not tui.progress("Desejas finalizar mesmo assim?"):
                return

        if session_status == SessionStatus.FINISHED:
            warnings.session_has_already_been_finished(clinic.current_session)
            return

    # ============= Desativa sessão atual =============

    clinic.current_session.status = SessionStatus.FINISHED

    # ============= Feedback =============

    tui.info(f"Sessão {clinic.current_session.date} finalizada!")
