from entities.clinic import Clinic

from menus.use_cases import condition
import tui


def annotate_medical_records(clinic: Clinic):
    """Faz anotação no prontuário do paciente atual.

    Feedbacks
    ---------
    * Ação concluída

    Warnings
    --------
    * Sessão não iniciada   : Propõe a iniciar
    * Sessão já finalizada
    * Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    if not condition.is_able_to_read_records(clinic):
        return

    # ============= Anotar =============

    note = tui.prompt(f"Anotar prontuário de {clinic.current_patient.name}:")
    clinic.current_patient.medical_records.append(
        f"{clinic.current_session.date}: {note}"
    )

    # ============= Feedback =============

    tui.info("Anotação feita!")
