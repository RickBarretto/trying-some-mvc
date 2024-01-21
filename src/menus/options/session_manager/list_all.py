from entities.clinic import ClinicModel
from tui.list import ListScreen


def list_all(clinic: ClinicModel):
        """Lista todas as sessões registradas na clínica.

        Feedbacks
        ---------
        * Lista de sessões. (data, id e status)
        * Se há ou não alguma registrada.
        """
        sessions = clinic.sessions
        
        data = sessions if sessions else ["Não há sessões registradas."]
        ListScreen("Sessões registradas:", data).render()