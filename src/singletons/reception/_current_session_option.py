from entities import clinic
import screen


class CurrentSessionOptions:
    @staticmethod
    def check_current_booking(clinic: clinic.ClinicController):
        """Verifica se paciente está agendado para a sessão atual.
        
        Questions
        ---------
        * CPF do paciente

        Feedbacks
        ---------
        * Status do agendamento

        Warnings
        --------
        * Paciente não registrado
        """

        # Entrada do CPF
        try:
            cpf = screen.Prompt.get_cpf()
        except ValueError as e:
            return screen.WarningScreen(e).render()

        patient = clinic.find_patient(cpf)

        # Verifica se paciente existe no banco de dados
        if not patient:
            return screen.WarningScreen("Paciente não registrado.").render()

        # Verifica se paciente está marcado para a sessão atual
        is_booked = clinic.model.current_session.uid in patient.scheduled_sessions

        # Imprime o feedback
        TEMPLATE_MESSAGE = "Paciente {} está marcado para a sessão atual."
        message = TEMPLATE_MESSAGE.format("" if is_booked else "não")

        screen.SplashScreen(message).render()
