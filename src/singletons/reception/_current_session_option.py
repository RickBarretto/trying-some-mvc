from entities import clinic
import screen


class CurrentSessionOptions:
    @staticmethod
    def check_current_booking(clinic: clinic.ClinicController):
        if (patient := clinic.find_patient(screen.Prompt.get_cpf())) is None:
            screen.WarningScreen("Paciente não registrado.").render()

        if clinic.get_patient_bookings(patient):
            screen.SplashScreen("Paciente está marcado para a sessão atual.").render()
        else:
            screen.SplashScreen(
                "Paciente não está marcado para a sessão atual."
            ).render()

    @staticmethod
    def send_to_waiting_queue(clinic: clinic.ClinicController):
        try:
            cpf = screen.Prompt.get_cpf()
        except ValueError as e:
            screen.WarningScreen(e).render()
        
        if clinic.push_to_queue(cpf):
            screen.WarningScreen("Fila atualizada.").render()
        else:
            screen.WarningScreen("Não há paciente na fila de espera.").render()

    @staticmethod
    def show_next_patient(clinic: clinic.ClinicController):
        if len(patients_ids := clinic.model.current_session.waiting_queue) < 2:
            screen.WarningScreen("Não há paciente na fila de espera.").render()
            return
        
        for patient in clinic.model.patients:
            if patient.uid == patients_ids[1]:
                break

        content = ["Próximo paciente:", clinic.view.format_patient(patient)]
        screen.SplashScreen(content).render()
