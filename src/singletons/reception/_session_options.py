from entities import clinic
import screen


class SessionOptions:

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