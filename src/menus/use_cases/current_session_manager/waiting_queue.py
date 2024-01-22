from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import SessionStatus

import tui

from menus.use_cases import propose, request, warnings


def send_to_waiting_queue(clinic: Clinic, patient: Patient | None = None) -> bool:
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
    * Sessão não inicializada   : Propõe a inicializar
    * Sessão já foi finalizada
    * Formato de CPF inválido
    * Paciente não registrado   : Propõe o registrar
    * Paciente não agendado     : Propõe o agendar para a sessão atual
    * Paciente já está na fila de espera

    """

    # Verifica status da sessão
    current_session_status = clinic.current_session.status

    if current_session_status == SessionStatus.UNBEGUN:
        warnings.session_has_never_started(clinic.current_session)
        if not propose.start_current_session(clinic):
            return 

    if current_session_status == SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return 

    # Valida a entrada do CPF
    if not patient:
        cpf = request.patient_cpf()
        patient = clinic.patient_by_cpf(cpf)

    if not patient:
        warnings.patient_not_registered(cpf)
        if propose.register_patient(clinic, cpf):
            patient = clinic.patient_by_cpf(cpf)
        else:
            return 

    # Verifica agendamento
    if clinic.current_session.uid not in patient.scheduled_sessions:
        tui.warn(f"{patient.name} não está agendado para a sessão atual!")
        if not propose.book_session(clinic, patient, clinic.current_session):
            return 

    # Verifica se o paciente já consta na fila de espera
    waiting_queue = clinic.waiting_queue
    if patient.uid in waiting_queue:
        tui.warn("Paciente já está na fila de espera.")
        return 

    # Põe o paciente na fila de espera
    clinic.waiting_queue.append(patient.uid)

    # Feedback

    tui.info(
        [
            f"{patient.name} colocado na fila de espera,",
            f"O mesmo se encontra na posição {len(waiting_queue)}!",
        ]
    )
