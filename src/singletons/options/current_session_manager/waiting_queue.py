from entities.clinic import ClinicController
from entities.session import SessionStatus

from screen.prompt import Prompt
from screen.warning import WarningScreen


def send_to_waiting_queue(clinic: ClinicController):
        
    # Valida a entrada do CPF
    try:
        cpf = Prompt.get_cpf()
    except ValueError as e:
        WarningScreen(e).render()

    # Verifica o status da sessão atual
    if clinic.model.current_session.status == SessionStatus.UNBEGUN:
        WarningScreen("A sessão atual nunca foi inicializada.").render()
        return
    
    if clinic.model.current_session.status == SessionStatus.UNBEGUN:
        WarningScreen("A sessão atual já foi finalizada.").render()
        return

    # Verifica se o paciente é registrado
    if (patient := clinic.find_patient(cpf)) is None:
        WarningScreen("Paciente não registrado.").render()
        return

    # Verifica se o paciente já consta na fila de espera
    if patient in clinic.model.waiting_queue:
        WarningScreen("Paciente já está na fila de espera.").render()
        return

    # Põe o paciente na fila de espera
    clinic.push_to_waiting_queue(patient)
    WarningScreen("Paciente colocado na fila de espera com sucesso!").render()
