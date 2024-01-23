from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import Session, SessionStatus

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

    # ============= Verifica status da sessão atual =============

    if session_has_never_begun(clinic.current_session):
        if not propose.start_current_session(clinic):
            return 

    if session_has_already_finished(clinic.current_session):
        return 

    # ============= Pega input do usuário =============

    if not patient:
        cpf = request.patient_cpf()
        patient = clinic.patient_by_cpf(cpf)

    # ============= Verifica registro do paciente =============

    if not patient:
        warnings.patient_not_registered(cpf)
        if not propose.register_patient(clinic, cpf):
            return
    
    patient = clinic.patient_by_cpf(cpf)

    # ============= Verifica agendamento do paciente =============

    if clinic.current_session.uid not in patient.scheduled_sessions:
        tui.warn(f"{patient.name} não está agendado para a sessão atual!")
        if not propose.book_session(clinic, patient, clinic.current_session):
            return

    # ============= Verifica se paciente está na fila =============
        
    if patient.uid in clinic.waiting_queue:
        tui.warn("Paciente já está na fila de espera.")
        return

    # ============= Põe paciente na fila =============

    clinic.waiting_queue.append(patient.uid)

    # ============= Feedback =============

    message = [
        f"{patient.name} colocado na fila de espera,",
        f"O mesmo se encontra na posição {len(clinic.waiting_queue)}!",
    ]

    tui.info(message)

def session_has_already_finished(session: Session):
    if res := (session.status == SessionStatus.FINISHED):
        warnings.session_has_never_started(session)

    return res

def session_has_never_begun(session: Session) -> bool:
    if res := (session.status == SessionStatus.UNBEGUN):
        warnings.session_has_already_been_finished(session)

    return res
