"""Casos de uso de avisos que se repetem durante o códugo."""

from entity.session import Session
import tui

__all__ = ["patient_not_registered", "session_not_registered", "session_has_already_started", "session_has_never_started", "session_has_already_been_finished"]

def patient_not_registered(patient_cpf: str):
    """Avisa que paciente não está registrado."""
    tui.warn(f"Não há paciente registrado para CPF {patient_cpf}!")


def session_not_registered(session_date: str):
    """Avisa que sessão não está registrada."""
    tui.warn(f"Não há sessão registrada para o dia {session_date}!")


def session_has_already_started(session: Session):
    """Avisa que sessão já foi iniciada."""
    tui.warn(f"A sessão {session.date} já foi iniciada!")


def session_has_never_started(session: Session):
    """Avisa que sessão nunca foi iniciada."""
    tui.warn(f"A sessão {session.date} nunca foi iniciada!")


def session_has_already_been_finished(session: Session):
    """Avisa que sessão já foi finalizada."""
    tui.warn(f"A sessão {session.date} já foi finalizada!")
