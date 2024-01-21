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

    @staticmethod
    def send_to_waiting_queue(clinic: clinic.ClinicController):
        
        # Valida a entrada do CPF
        try:
            cpf = screen.Prompt.get_cpf()
        except ValueError as e:
            screen.WarningScreen(e).render()

        # Verifica o status da sessão atual
        if clinic.model.current_session.status == SessionStatus.UNBEGUN:
            screen.WarningScreen("A sessão atual nunca foi inicializada.").render()
            return
        
        if clinic.model.current_session.status == SessionStatus.UNBEGUN:
            screen.WarningScreen("A sessão atual já foi finalizada.").render()
            return

        # Verifica se o paciente é registrado
        if (patient := clinic.find_patient(cpf)) is None:
            screen.WarningScreen("Paciente não registrado.").render()
            return

        # Verifica se o paciente já consta na fila de espera
        if patient in clinic.model.waiting_queue:
            screen.WarningScreen("Paciente já está na fila de espera.").render()
            return

        # Põe o paciente na fila de espera
        clinic.push_to_waiting_queue(patient)
        screen.WarningScreen("Paciente colocado na fila de espera com sucesso!").render()

