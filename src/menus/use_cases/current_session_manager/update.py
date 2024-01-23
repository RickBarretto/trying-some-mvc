from entities.clinic import Clinic
from entities.session import Session

import tui



def update(clinic: Clinic, session: Session) -> bool:
    """Atualiza a sessão atual.

    Note
    ----
    Essa função em específica deve ser chamada pelo sistema em certas circunstâncias,
    e nunca pelo usuário.

    Feedbacks
    ---------
    * Sessão atual atualizada

    """

    # ============= Atualiza sessão atual =============

    clinic.current_session = session

    # ============= Feedback =============

    tui.info(f"Sessão atual atualizada para o dia {session.date}!")
