from entities.clinic import ClinicController
from tui import WarningScreen, SplashScreen


def show_next_patient(clinic: ClinicController):
    """Mostra novo paciente

    Questions
    ---------
    * Nenhuma

    Feedbacks
    ---------
    * Informações básicas do paciente

    Warnings
    --------
    * Não há pacientes na fila
    """
    waiting_queue = clinic.model.waiting_queue

    # Verifica se a fila de espera está vazia
    if not waiting_queue:
        WarningScreen("Não há pacientes na fila de espera.").render()
        return

    # Pega a instância do próximo paciente
    next_patient_id = waiting_queue[0]
    patient = clinic.patient_by_id(next_patient_id)

    # Imprime informações do paciente
    content = ["Próximo paciente:", clinic.view.format_patient(patient)]
    SplashScreen(content).render()
