from entities import clinic
import screen


class PatientOptions:
    @staticmethod
    def register_patient(clinic: clinic.ClinicController):
        try:
            cpf: str = screen.Prompt.get_cpf()
            name: str = screen.Prompt.prompt("Insira o nome do paciente.")
            extra: str = screen.Prompt.multiline("Insira informações extra.")
        except ValueError as e:
            screen.WarningScreen(e).render()

        if clinic.register_patient(cpf, name, extra):
            screen.WarningScreen("Paciente registrado com sucesso!").render()
        else:
            screen.WarningScreen("Paciente já foi registrado.").render()

    @staticmethod
    def book_schedule(clinic: clinic.ClinicController):
        """Agenda uma sessão para um paciente.
        
        Questions
        ---------
        * CPF do paciente
        * Data da sessão

        Feedbacks
        ---------
        * Status do agendamento

        Warnings
        --------
        * Formato de data inválido
        * Formato de CPF inválido
        * Paciente não registrado
        * Sessão não registrada
        * Sessão já finalizada
        * Paciente já estava agendado
        """

        # Valida entradas
        try:
            patient_cpf = screen.Prompt.get_cpf()
            session_date = screen.Prompt.get_date()
        except ValueError as e:
            screen.WarningScreen(e).render()
            return

        patient = clinic.find_patient(patient_cpf)
        session = clinic.find_session(session_date)

        # Valida registros
        if not patient:
            screen.WarningScreen("Paciente não registrado.").render()
            return
        
        if not session:
            screen.WarningScreen("Sessão não registrada.").render()
            return

        # Verifica o agendamento
        if session.uid in patient.scheduled_sessions:
            screen.WarningScreen(
                f"Paciente {patient.name} já está "\
                f"registrado para a sessão {session.formated_date}."
            ).render()
            return

        # Agenda sessão para paciente
        clinic.book_schedule(patient, session)
        screen.WarningScreen("Paciente agendado com sucesso!").render()

    @staticmethod
    def list_patient_bookings(clinic: clinic.ClinicController):
        try:
            cpf = screen.Prompt.get_cpf()

            if (patient := clinic.find_patient(cpf)) is None:
                screen.WarningScreen("Paciente não registrado.").render()
                return

            if sessions := clinic.get_patient_bookings(patient):
                screen.ListScreen("Sessões agendadas", sessions).render()
            else:
                screen.WarningScreen("Paciente não possui sessões agendadas.").render()

        except ValueError as e:
            screen.WarningScreen(e).render()
            return
