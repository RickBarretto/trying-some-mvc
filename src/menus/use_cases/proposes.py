from typing import Callable

from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import Session
from menus.use_cases import current_session_manager, patient_manager, session_manager
import tui


def _propose(question: str, use_case: Callable, *args, **kwargs) -> bool:
    if tui.progress(question):
        use_case(*args, **kwargs)
        return True
    return False


def add_to_waiting_queue(clinic: Clinic, patient: Patient) -> bool:
    question = f"Desejas adicionar {patient.name} à fila de espera?"
    use_case = current_session_manager.send_to_waiting_queue

    return _propose(question, use_case, clinic, patient)


def send_patient_to_waiting_queue(clinic: Clinic, patient: Patient) -> bool:
    question = f"Desejas encaminhar {patient.name} para fila de espera?"
    use_case = current_session_manager.send_to_waiting_queue

    return _propose(question, use_case, clinic, patient)


def start_current_session(clinic: Clinic) -> bool:
    question = "Desejas iniciar sessão atual?"
    use_case = current_session_manager.start

    return _propose(question, use_case, clinic)


def register_patient(clinic: Clinic, patient_cpf: str) -> bool:
    question = f"Desejas registar paciente do CPF {patient_cpf}?"
    use_case = patient_manager.register

    return _propose(question, use_case, clinic, patient_cpf)


def book_session(clinic: Clinic, patient: Patient, session: Session) -> bool:
    question = f"Desejas agendar {patient.name} para {session.date}?"
    use_case = patient_manager.book_schedule

    return _propose(question, use_case, clinic, patient, session)


def register_session(clinic: Clinic, session_date: str) -> bool:
    question = f"Desejas registar sessão na data {session_date}?"
    use_case = session_manager.register

    return _propose(question, use_case, clinic, date=session_date)
