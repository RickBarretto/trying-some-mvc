import entities
from menus.use_cases import condition
import tui


def annotate_medical_records(clinic: entities.Clinic):
    """Faz anotação no prontuário do paciente atual.

    Questions
    ---------
    Anotação

    Feedbacks
    ---------
    Ação concluída

    Warnings                            Proposes
    --------                            --------
    Sessão atual não iniciada           Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    is_able_to_read = condition.has_patient_being_attended and \
        condition.has_active_current_session_or_activate_it(clinic)
    
    if not is_able_to_read:
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
