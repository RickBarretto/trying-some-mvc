from entities.clinic import ClinicController
from tui.list import ListScreen


def list_all(clinic: ClinicController):
        """Lista todas as sessões registradas na clínica.

        Feedbacks
        ---------
        * Lista de sessões. (data, id e status)
        * Se há ou não alguma registrada.
        """
        sessions = clinic.get_sessions()
        
        data = sessions if sessions else ["Não há sessões registradas."]
        ListScreen("Sessões registradas:", data).render()