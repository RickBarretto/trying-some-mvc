from entities.clinic import Clinic
from entities.patient import Patient
import tui
from menus.use_cases import propose, request, warnings


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

    # ============= Verificação do paciente no banco de dados =============

    cpf = request.patient_cpf()

    if not (patient := clinic.patient_by_cpf(cpf)):
        warnings.patient_not_registered(cpf)

        if propose.register_patient(clinic, cpf):
            patient = clinic.patient_by_cpf(cpf)
        else:
            return

    # ============= Verificação do agendamento =============

    is_booked = clinic.current_session.uid in patient.scheduled_sessions

    # ============= Impressão do feedback =============

    show_checking_feedback(patient, is_booked)

    # ============= Proposta de agendamento =============

    if not is_booked:
        if not propose.book_session(clinic, patient, clinic.current_session):
            return

    # ============= Enfileiramento do paciente =============

    propose.send_patient_to_waiting_queue(clinic, patient)


def show_checking_feedback(patient: Patient, is_booked: bool):
    message_start = patient.name + " " + ("" if is_booked else "não")
    message_end = "está marcado para a sessão atual"

    tui.info(f"{message_start} {message_end}")
