from entities.clinic import Clinic
from tui.list import ListScreen

from menus.use_cases import status


def list_all(clinic: Clinic):
    """Lista todas as sessões registradas na clínica.

    Feedbacks
    ---------
    * Lista de sessões. (data, id e status)
    * Se há ou não alguma registrada.

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """
    sessions = clinic.sessions

    data = sessions if sessions else ["Não há sessões registradas."]
    ListScreen("Sessões registradas:", data).render()

    return status.Ok
