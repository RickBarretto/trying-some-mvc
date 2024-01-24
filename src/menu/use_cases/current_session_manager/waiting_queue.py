import entity
import tui
from menu.use_cases.commons import condition, fetch, propose

__all__ = ["send_to_waiting_queue"]

def send_to_waiting_queue(clinic: entity.Clinic, patient: entity.Patient | None = None):
    """Envia um paciente para a fila de espera.

    Questions
    ---------
    CPF do paciente

    Feedbacks
    ---------
    Paciente posto na fila de espera
    Posição na fila de espera

    Warnings                                Proposes
    --------                                --------
    Sessão não inicializada                 Iniciar sessão atual
    Sessão já foi finalizada
    CPF inválido
    Paciente não registrado                 Registrar paciente
    Paciente não agendado                   Agendar paciente para a sessão atual
    Paciente já está na fila de espera

    """

    # ============= Verifica status da sessão atual =============

    if not condition.has_active_current_session_or_activate_it(clinic):
        return

    # ============= Pega input do usuário =============

    if not patient:
        if not (patient := fetch.patient_or_register(clinic)):
            return

    # ============= Verifica agendamento do paciente =============

    if clinic.current_session.uid not in patient.scheduled_sessions:
        tui.warn(f"{patient.name} não está agendado para a sessão atual!")
        if not propose.book_session(clinic, patient, clinic.current_session):
            return

    # ============= Verifica se paciente está na fila =============

    if patient.uid in clinic.waiting_queue:
        tui.warn("Paciente já está na fila de espera!")
        return

    # ============= Põe paciente na fila =============
    _send_patient_to_queue(clinic, patient)


def _send_patient_to_queue(clinic: entity.Clinic, patient: entity.Patient):
    clinic.waiting_queue.append(patient.uid)

    message = [
        f"{patient.name} colocado na fila de espera",
        f"O mesmo se encontra na posição {len(clinic.waiting_queue)}.",
    ]

    tui.info(message)
