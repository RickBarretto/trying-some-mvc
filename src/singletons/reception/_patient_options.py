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
        try:
            if (patient := clinic.find_patient(screen.Prompt().get_cpf())) is None:
                screen.WarningScreen("Paciente não registrado.").render()
                return

            if (session := clinic.find_session(screen.Prompt().get_date())) is None:
                screen.WarningScreen("Sessão não registrada.").render()
                return

        except ValueError as e:
            screen.WarningScreen(e).render()
            return

        if clinic.book_schedule(patient, session):
            screen.WarningScreen("Paciente agendado com sucesso!").render()
        else:
            screen.WarningScreen("Paciente já estava agendado.").render()

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
