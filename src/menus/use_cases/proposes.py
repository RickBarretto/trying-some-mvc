from entities.clinic import Clinic
from entities.patient import Patient
from entities.session import Session
from menus.use_cases import current_session_manager, patient_manager, session_manager
import tui


def add_to_waiting_queue(clinic: Clinic, patient: Patient) -> bool:
    if tui.progress(f"Desejas adicionar {patient.name} à fila de espera?"):
        current_session_manager.send_to_waiting_queue(clinic, patient)
        return True

    return False


def send_patient_to_waiting_queue(clinic: Clinic, patient: Patient) -> bool:
    if tui.progress(f"Desejas encaminhar {patient.name} para fila de espera?"):
        current_session_manager.send_to_waiting_queue(clinic, patient)
        return True

    return False


def start_current_session(clinic: Clinic) -> bool:
    if tui.progress("Desejas iniciar sessão atual?"):
        current_session_manager.start(clinic)
        return True

    return False


def register_patient(clinic: Clinic, patient_cpf: str) -> bool:
    if tui.progress(f"Desejas registar paciente do CPF {patient_cpf}?"):
        patient_manager.register(clinic, patient_cpf)
        return True

    return False


def book_session(clinic: Clinic, patient: Patient, session: Session) -> bool:
    if tui.progress(f"Desejas agendar {patient.name} para {session.date}?"):
        patient_manager.book_schedule(clinic, patient, session)
        return True

    return False


def register_session(clinic: Clinic, session_date: str) -> bool:
    if tui.progress(f"Desejas registar sessão na data {session_date}?"):
        session_manager.register(clinic, date=session_date)
        return True

    return False
