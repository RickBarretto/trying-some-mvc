import entity
import tui
from menu.use_cases.commons import fetch

__all__ = ["list_bookings"]

def list_bookings(clinic: entity.Clinic):
    """Lista os agendamentos de um paciente.

    Questions
    ---------
    CPF do paciente

    Feedbacks
    ---------
    Lista de agendamentos
    Nenhum agendamento

    Warnings                    Proposes
    --------                    --------
    Formato de CPF inválido
    Paciente não registrado     Registrar paciente

    """

    # ============= Verifica registro do paciente =============

    if not (patient := fetch.patient_or_register(clinic)):
        return

    # ============= Lista agendamentos =============

    tui.bullet_list(
        f"Sessões agendadas de {patient.name}:", find_bookings(clinic, patient)
    )


def find_bookings(clinic: entity.Clinic, patient: entity.Patient) -> list[str]:
    sessions_ids = patient.scheduled_sessions
    sessions = [
        str(session) for session in clinic.sessions if session.uid in sessions_ids
    ]

    return sessions if sessions else ["Nenhuma sessão agendada"]
