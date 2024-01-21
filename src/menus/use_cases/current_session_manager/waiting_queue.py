from entities.clinic import Clinic
from entities.session import SessionStatus

from tui.prompt import Prompt
from tui.warning import WarningScreen


def send_to_waiting_queue(clinic: Clinic):
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
    current_session_status = clinic.current_session.status

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
    patient = clinic.patient_by_cpf(cpf) 
    if not patient:
        WarningScreen("Paciente não registrado.").render()
        return


    # Verifica se o paciente já consta na fila de espera
    waiting_queue = clinic.waiting_queue
    if patient.uid in waiting_queue:
        WarningScreen("Paciente já está na fila de espera.").render()
        return

    # Põe o paciente na fila de espera
    clinic.waiting_queue.append(patient.uid)
    WarningScreen(f"Paciente colocado na fila de espera na posição {len(waiting_queue)}!").render()
