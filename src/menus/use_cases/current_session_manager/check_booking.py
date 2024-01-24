import entities
from menus.use_cases import fetch, propose
import tui


def check_current_booking(clinic: entities.Clinic):
    """Verifica se paciente está agendado para a sessão atual.

    Questions
    ---------
    CPF do paciente

    Feedbacks
    ---------
    Status do agendamento

    Warnings                    Proposes
    --------                    --------
    CPF inválido
    Paciente não registrado     Registrar paciente
    [ok]                        Agendar sessão
    [ok]                        Enviar paciente para fila de espera

    """

    # ============= Verificação do paciente no banco de dados =============

    if not (patient := fetch.patient_or_register(clinic)):
        return

    # ============= Verificação do agendamento =============

    is_booked = clinic.current_session.uid in patient.scheduled_sessions
    show_checking_feedback(patient, is_booked)

    # ============= Proposta de agendamento =============

    if not is_booked:
        if not propose.book_session(clinic, patient, clinic.current_session):
            return

    # ============= Proposta de enfileiramento do paciente =============

    propose.send_patient_to_waiting_queue(clinic, patient)


def show_checking_feedback(patient: entities.Patient, is_booked: bool):
    message_start = patient.name + " " + ("" if is_booked else "não")
    message_end = "está marcado para a sessão atual"

    tui.info(f"{message_start} {message_end}")
