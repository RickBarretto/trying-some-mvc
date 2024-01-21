from entities import clinic
import screen


class PatientOptions:

    @staticmethod
    def list_patient_bookings(clinic: clinic.ClinicController):
        """Lista os agendamentos de um paciente.

        Questions
        ---------
        * CPF do paciente

        Feedbacks
        ---------
        * Lista de agendamentos
        * Nenhum agendamento

        Warnings
        --------
        * Formato de CPF inválido
        * Paciente não registrado
        """

        # Valida entrada
        try:
            cpf = screen.Prompt.get_cpf()
        except ValueError as e:
            screen.WarningScreen(e).render()
            return

        patient = clinic.find_patient(cpf)

        # Verifica registro
        if patient is None:
            screen.WarningScreen("Paciente não registrado.").render()
            return

        # Lista sessões agendadas
        booked_sessions = clinic.get_patient_bookings(patient)
        data = booked_sessions if booked_sessions else ["Nenhuma sessão agendada"]

        screen.ListScreen("Sessões agendadas", data).render()
