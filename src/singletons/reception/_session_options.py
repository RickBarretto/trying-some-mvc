from entities import clinic
import screen


class SessionOptions:
    @staticmethod
    def register_session(clinic: clinic.ClinicController):
        """Agenda uma sessão para um paciente.

        Questions
        ---------
        * Data da sessão

        Feedbacks
        ---------
        * Status do registro

        Warnings
        --------
        * Formato de data inválido
        * Sessão já registrada
        """

        # Valida entrada
        try:
            date = screen.Prompt.get_date()
        except ValueError as e:
            screen.WarningScreen(e).render()
            return
        
        # Verifica registro
        session = clinic.find_session(date)
        if session:
            screen.WarningScreen("Sessão já foi registrada.").render()
            return

        # Registra sessão
        session = clinic.register_session(date)
        screen.WarningScreen(f"Sessão registrada na data {session.formated_date}.").render()

    @staticmethod
    def list_sessions(clinic: clinic.ClinicController):
        sessions = clinic.get_sessions()
        if not sessions:
            screen.WarningScreen("Não há sessões registradas.").render()
        else:
            screen.ListScreen("Sessões registradas:", sessions).render()

    @staticmethod
    def find_session(clinic: clinic.ClinicController):
        try:
            date = screen.Prompt().get_date()
        except ValueError as e:
            screen.WarningScreen(e).render()
            return

        if clinic.find_session(date):
            screen.WarningScreen("Sessão encontrada.").render()
        else:
            screen.WarningScreen("Sessão não encontrada.").render()