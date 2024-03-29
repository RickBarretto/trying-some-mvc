from typing import Callable

import entity
from app.use_cases import current_session_manager, patient_manager, session_manager
import tui

__all__ = [
    "send_patient_to_waiting_queue",
    "start_current_session",
    "register_patient",
    "book_session",
    "register_session",
]

# ============= Gerencia sessão atual =============


def send_patient_to_waiting_queue(
    clinic: entity.Clinic, patient: entity.Patient
) -> bool:
    """Propõe enviar o paciente para a fila de espera"""
    question = f"Desejas encaminhar {patient.name} para fila de espera?"
    use_case = current_session_manager.send_to_waiting_queue

    return _propose(question, use_case, clinic, patient)


def start_current_session(clinic: entity.Clinic) -> bool:
    """Propõe iniciar a sessão atual"""
    question = "Desejas iniciar sessão atual?"
    use_case = current_session_manager.start

    return _propose(question, use_case, clinic)


# ============= Gerencia pacientes =============


def register_patient(clinic: entity.Clinic, patient_cpf: str) -> bool:
    """Propõe registrar o paciente"""
    question = f"Desejas registar paciente do CPF {patient_cpf}?"
    use_case = patient_manager.register

    return _propose(question, use_case, clinic, patient_cpf)


def book_session(
    clinic: entity.Clinic, patient: entity.Patient, session: entity.Session
) -> bool:
    """Propõe agendar uma sessão"""
    question = f"Desejas agendar {patient.name} para {session.date}?"
    use_case = patient_manager.book_schedule

    return _propose(question, use_case, clinic, patient, session)


# ============= Gerencia sessões gerais =============


def register_session(clinic: entity.Clinic, session_date: str) -> bool:
    """Propõe registar uma sessão"""
    question = f"Desejas registar sessão na data {session_date}?"
    use_case = session_manager.register

    return _propose(question, use_case, clinic, date=session_date)


# ============= Função interna =============


def _propose(question: str, use_case: Callable, *args, **kwargs) -> bool:
    """Função que faz a interface para as propostas deste módulo.

    Arguments
    ---------
    question: str
        A pergunta a ser feita
    use_case: Callable
        A função do caso de uso a ser chamada
    *args, **kwargs
        Os argumentos a serem passados para ``use_case``
    """
    if tui.proceed(question):
        use_case(*args, **kwargs)
        return True
    return False
