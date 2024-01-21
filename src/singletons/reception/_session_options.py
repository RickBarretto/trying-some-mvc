from entities import clinic
import screen


class SessionOptions:
    @staticmethod
    def add_session(clinic: clinic.ClinicController):
        try:
            date = screen.Prompt.get_date()
        except ValueError as e:
            screen.WarningScreen(e).render()
            return

        if not clinic.register_session(date):
            screen.WarningScreen("Sessão já foi registrada.").render()
        else:
            screen.WarningScreen("Sessão registrada.").render()

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

    @staticmethod
    def start_session(clinic: clinic.ClinicController):
        if clinic.start_session():
            screen.WarningScreen("Sessão iniciada!").render()
        else:
            screen.WarningScreen("Sessão já foi iniciada ou finalizada.").render()
