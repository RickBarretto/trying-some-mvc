from entities import clinic
from entities.session import SessionStatus
import screen


class CurrentSessionOptions:
    @staticmethod
    def check_current_booking(clinic: clinic.ClinicController):

        # Entrada do CPF
        try:
            cpf = screen.Prompt.get_cpf()
        except ValueError as e:
            return screen.WarningScreen(e).render()

        # Verifica se paciente existe no banco de dados
        if (patient := clinic.find_patient(cpf)) is None:
            return screen.WarningScreen("Paciente não registrado.").render()

        # Verifica se paciente está marcado para a sessão atual
        bookings = clinic.get_patient_bookings(patient)
        
        if bookings:
            screen.SplashScreen("Paciente está marcado para a sessão atual.").render()
        else:
            screen.SplashScreen(
                "Paciente não está marcado para a sessão atual."
            ).render()
