from entities import clinic
import screen


class PatientOptions:
    @staticmethod
    def register_patient(clinic: clinic.ClinicController):
        """Registra paciente no banco de dados.

        Questions
        ---------
        * CPF do paciente
        * Nome do paciente
        * Informações extras

        Feedbacks
        ---------
        * Registro foi um sucesso

        Warnings
        --------
        * Formato de CPF inválido
        * TODO: Nome não deve conter números ou símbolos
        * TODO: Nome deve conter pelo menos nome e sobrenome
        * Paciente já registrado
        """

        # Valida entradas
        try:
            cpf: str = screen.Prompt.get_cpf()
            name: str = screen.Prompt.prompt("Insira o nome do paciente.")
            extra: str = screen.Prompt.multiline("Insira informações extra.")
        except ValueError as e:
            screen.WarningScreen(e).render()
            return

        # Verifica se paciente já está registrado
        if clinic.find_patient(cpf):
            screen.WarningScreen("Paciente já foi registrado.").render()
            return

        # Registra paciente
        patient = clinic.register_patient(cpf, name, extra)
        screen.WarningScreen(f"{patient.name} registrado com sucesso!").render()

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
                f"Paciente {patient.name} já está "
                f"registrado para a sessão {session.formated_date}."
            ).render()
            return

        # Agenda sessão para paciente
        clinic.book_schedule(patient, session)
        screen.WarningScreen("Paciente agendado com sucesso!").render()

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
