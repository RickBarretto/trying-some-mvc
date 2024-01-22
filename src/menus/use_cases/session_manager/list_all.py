from entities.clinic import Clinic
import tui



def list_all(clinic: Clinic):
    """Lista todas as sessões registradas na clínica.

    Feedbacks
    ---------
    * Lista de sessões. (data, id e status)
    * Se há ou não alguma registrada.

    """
    sessions = clinic.sessions

    data = sessions if sessions else ["Não há sessões registradas."]
    tui.bullet_list("Sessões registradas:", data)
