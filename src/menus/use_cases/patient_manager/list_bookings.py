import entities
import tui
from menus.use_cases import commons


def list_bookings(clinic: entities.Clinic):
    """Lista os agendamentos de um paciente.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Lista de agendamentos
    * Nenhum agendamento

    Warnings                    Proposes
    --------                    --------
    Formato de CPF inválido
    Paciente não registrado     Registrar paciente

    """

    # ============= Verifica registro do paciente =============

    if not (patient := commons.get_patient(clinic)):
        return

    # ============= Lista agendamentos =============

    tui.bullet_list(
        f"Sessões agendadas de {patient.name}:", find_bookings(clinic, patient)
    )


def find_bookings(clinic: entities.Clinic, patient: entities.Patient) -> list[str]:
    sessions_ids = patient.scheduled_sessions
    sessions = [
        str(session) for session in clinic.sessions if session.uid in sessions_ids
    ]

    return sessions if sessions else ["Nenhuma sessão agendada"]
