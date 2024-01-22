from entities.session import Session
import tui

def patient_not_registered(patient_cpf: str):
    tui.warn(f"Paciente não registrado para CPF {patient_cpf}.")

def session_was_never_started(session: Session):
    tui.warn(f"A sessão {session.date} nunca foi iniciada!")

def session_already_was_finished(session: Session):
    tui.warn(f"A sessão {session.date} já foi finalizada!")
