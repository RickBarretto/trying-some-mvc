import entities
from menus.use_cases import condition
import tui


def annotate_medical_records(clinic: entities.Clinic):
    """Faz anotação no prontuário do paciente atual.

    Feedbacks
    ---------
    * Ação concluída

    Warnings                            Proposes
    --------                            --------
    * Sessão não iniciada               * Propõe iniciar sessão
    * Sessão já finalizada
    * Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    if not condition.is_able_to_read_records(clinic):
        return

    # ============= Anota no prontuário =============

    message = f"Anotar prontuário de {clinic.current_patient.name}:"
    annotation = tui.prompt(message)
    save_annotation(clinic, annotation)

    # ============= Feedback =============

    tui.info("Anotação feita!")


def save_annotation(clinic: entities.Clinic, note: str):
    """Formata e salva a anotação no prontuário."""
    formated_note = f"{clinic.current_session.date}: {note}"
    clinic.current_patient.medical_records.append(formated_note)
