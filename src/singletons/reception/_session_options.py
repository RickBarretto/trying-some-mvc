from entities import clinic
import screen


class SessionOptions:

    @staticmethod
    def list_sessions(clinic: clinic.ClinicController):
        """Lista todas as sessões registradas na clínica.

        Feedbacks
        ---------
        * Lista de sessões. (data, id e status)
        * Se há ou não alguma registrada.
        """
        sessions = clinic.get_sessions()
        
        data = sessions if sessions else ["Não há sessões registradas."]
        screen.ListScreen("Sessões registradas:", data).render()

    @staticmethod
    def find_session(clinic: clinic.ClinicController):
        """Registra uma nova sessão no banco de dados.

        Questions
        ---------
        * Data da sessão

        Feedbacks
        ---------
        * Informações básicas da sessão

        Warnings
        --------
        * Formato de data inválido
        * Sessão não registrada
        """

        # Valida entrada
        try:
            date = screen.Prompt().get_date()
        except ValueError as e:
            screen.WarningScreen(e).render()
            return
        
        # Valida entrada
        session = clinic.find_session(date)

        if session:
            screen.WarningScreen(["Sessão encontrada.", session.formated_date, str(session.status)]).render()
        else:
            screen.WarningScreen("Sessão não encontrada.").render()