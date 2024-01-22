from entities.clinic import Clinic
import tui

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
        Retorna o status da função, que pode ser `status.Ok` (`False`)
        ou `status.MayBeRepeated` (`True`).
    """
    sessions = clinic.sessions

    data = sessions if sessions else ["Não há sessões registradas."]
    tui.bullet_list("Sessões registradas:", data)

    return status.Ok
