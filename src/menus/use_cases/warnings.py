from entities.session import Session
import tui

def patient_not_registered(patient_cpf: str):
    tui.warn(f"Não há paciente registrado para CPF {patient_cpf}.")


def session_has_already_started(session: Session):
    tui.warn(f"A sessão {session.date} já foi iniciada!")

def session_has_never_started(session: Session):
    tui.warn(f"A sessão {session.date} nunca foi iniciada!")

def session_has_already_been_finished(session: Session):
    tui.warn(f"A sessão {session.date} já foi finalizada!")
