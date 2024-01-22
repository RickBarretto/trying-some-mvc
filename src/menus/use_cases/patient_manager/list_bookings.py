from entities.clinic import Clinic
from tui import prompt

import tui

from menus.use_cases import propose, request, status


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

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Valida entrada

    cpf = request.patient_cpf
    patient = clinic.patient_by_cpf(cpf)

    # Verifica registro

    if patient is None:
        tui.warn("Paciente não registrado.")
        if propose.register_patient(clinic, cpf):
            patient = clinic.patient_by_cpf(cpf)
        else:
            return status.Ok

    # Lista sessões agendadas

    sessions_ids = patient.scheduled_sessions
    sessions = [session for session in clinic.sessions if session.uid in sessions_ids]

    data = sessions if sessions else ["Nenhuma sessão agendada"]

    tui.bullet_list(f"Sessões agendadas de {patient.name}:", data)
    return status.Ok
