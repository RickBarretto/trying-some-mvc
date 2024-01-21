from entities.clinic import ClinicController
from entities.session import SessionStatus

from screen.prompt import Prompt
from screen.warning import WarningScreen


def send_to_waiting_queue(clinic: ClinicController):
    """Envia um paciente para a fila de espera.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Paciente posto na fila de espera
    * Posição na fila de espera

    Warnings
    --------
    * Sessão não inicializada
    * Sessão já foi finalizada
    * Formato de CPF inválido
    * Paciente não registrado
    * Paciente já está na fila de espera
    """

    # Verifica status da sessão
    current_session_status = clinic.model.current_session.status

    if current_session_status == SessionStatus.UNBEGUN:
        WarningScreen("A sessão nunca foi inicializada.").render()
        return
    
    if current_session_status == SessionStatus.FINISHED:
        WarningScreen("A sessão ja foi finalizada.").render()
        return

    # Valida a entrada do CPF
    try:
        cpf = Prompt.get_cpf()
    except ValueError as e:
        WarningScreen(e).render()


    # Verifica se o paciente é registrado
    patient = clinic.find_patient(cpf) 
    if not patient:
        WarningScreen("Paciente não registrado.").render()
        return


    # Verifica se o paciente já consta na fila de espera
    waiting_queue = clinic.model.waiting_queue
    if patient.uid in waiting_queue:
        WarningScreen("Paciente já está na fila de espera.").render()
        return

    # Põe o paciente na fila de espera
    clinic.push_to_waiting_queue(patient)
    WarningScreen(f"Paciente colocado na fila de espera na posição {len(waiting_queue)}!").render()
