from entities import clinic
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
        
        # Entrada do CPF
        try:
            cpf = screen.Prompt.get_cpf()
        except ValueError as e:
            screen.WarningScreen(e).render()
        
        # Coloca paciente na fila
        if status := clinic.push_to_queue(cpf):
            screen.WarningScreen("Fila atualizada.").render()
        else:
            screen.WarningScreen("Não há paciente na fila de espera.").render()

    @staticmethod
    def show_next_patient(clinic: clinic.ClinicController):

        # TODO: atualizar a forma que temos o paciente atual e o próximo
        # Se temos apenas um paciente na fila, e nenhum em atendimento,
        # quem seria o próximo?
        #
        # Portanto, adicionar ``current_patient``  em ``ClinicalModel``  

        # Verifica se há dois pacientes na fila de espera
        if len(patients_ids := clinic.model.waiting_queue) < 2:
            screen.WarningScreen("Não há paciente na fila de espera.").render()
            return
        
        # Procura a instância do paciente
        for patient in clinic.model.patients:
            if patient.uid == patients_ids[1]:
                break

        # Imprime informações do paciente
        content = ["Próximo paciente:", clinic.view.format_patient(patient)]
        screen.SplashScreen(content).render()
