
from entities.clinic import ClinicController
from screen import WarningScreen, SplashScreen 


def show_next_patient(clinic: ClinicController):
    """Mostra novo paciente
    
    Questions
    ---------
    * Nenhuma

    Feedbacks
    ---------
    * Informações básicas do paciente

    Error Reports
    -------------
    * Se não houver pacientes na fila
    """
    waiting_queue = clinic.model.waiting_queue

    # Verifica se a fila de espera está vazia 
    if not waiting_queue:
        WarningScreen("Não há pacientes na fila de espera.").render()
        return

    # Pega a instância do próximo paciente
    next_patient_id = waiting_queue[0]
    patient = clinic.get_patient(next_patient_id)

    # Imprime informações do paciente
    content = ["Próximo paciente:", clinic.view.format_patient(patient)]
    SplashScreen(content).render()