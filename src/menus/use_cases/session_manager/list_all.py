from entities.clinic import Clinic
import tui


def list_all(clinic: Clinic):
    """Lista todas as sessões registradas na clínica.

    Feedbacks
    ---------
    Lista de sessões
    Se há ou não alguma registrada

    """

    # ============= Lista sessões =============

    data = (
        [str(session) for session in clinic.sessions]
        if clinic.sessions
        else ["Não há sessões registradas."]
    )
    tui.bullet_list("Sessões registradas:", data)
