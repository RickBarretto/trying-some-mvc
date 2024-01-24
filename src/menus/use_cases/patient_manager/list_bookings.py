from entities.clinic import Clinic
from entities.patient import Patient

import tui

from menus.use_cases import propose, request, warnings


def list_bookings(clinic: Clinic):
    """Lista os agendamentos de um paciente.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Lista de agendamentos
    * Nenhum agendamento

    Warnings
    --------
    * Formato de CPF inválido
    * Paciente não registrado   : Propõe o registrar

    """

    # ============= Verifica registro do paciente =============

    cpf = request.patient_cpf()
    patient = clinic.patient_by_cpf(cpf)

    if not patient:
        warnings.patient_not_registered(cpf)
        if not propose.register_patient(clinic, cpf):
            return

        patient = clinic.patient_by_cpf(cpf)

    # ============= Lista agendamentos =============

    tui.bullet_list(
        f"Sessões agendadas de {patient.name}:", find_bookings(clinic, patient)
    )


def find_bookings(clinic: Clinic, patient: Patient) -> list[str]:
    sessions_ids = patient.scheduled_sessions
    sessions = [
        str(session) for session in clinic.sessions if session.uid in sessions_ids
    ]

    return sessions if sessions else ["Nenhuma sessão agendada"]
