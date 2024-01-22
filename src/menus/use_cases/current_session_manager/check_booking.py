from entities.clinic import Clinic
import tui
from menus.use_cases import propose, request


def check_current_booking(clinic: Clinic):
    """Verifica se paciente está agendado para a sessão atual.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Status do agendamento

    Warnings
    --------
    * Paciente não registrado   : Propõe o registrar.
    
    """

    # Entrada do CPF
    cpf = request.patient_cpf()

    # Verifica se paciente existe no banco de dados

    if not (patient := clinic.patient_by_cpf(cpf)):
        tui.warn("Paciente não registrado.")

        if propose.register_patient(clinic, cpf):
            patient = clinic.patient_by_cpf(cpf)
        else:
            return

    # Verifica se paciente está marcado para a sessão atual
    is_booked = clinic.current_session.uid in patient.scheduled_sessions

    # Imprime o feedback

    TEMPLATE_MESSAGE = "Paciente {}{}está marcado para a sessão atual."
    message = TEMPLATE_MESSAGE.format(patient.name, " " if is_booked else " não ")

    tui.info(message)

    if not is_booked:
        if not propose.book_session(clinic, patient, clinic.current_session):
            return

    propose.send_patient_to_waiting_queue(clinic, patient)
