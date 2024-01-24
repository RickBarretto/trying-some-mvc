from entities.clinic import Clinic
from menus.use_cases import condition
import tui

__all__ = [
    "read_first_medical_annotation",
    "read_full_medical_records",
    "read_last_medical_annotation",
]


def read_full_medical_records(clinic: Clinic):
    """Lê o prontuário médico completo do paciente atual.

    Feedbacks
    ---------
    * Listagem das anotações
    * Se há anotações

    Warnings
    --------
    * Sessão não iniciada   : Propõe a iniciar
    * Sessão já finalizada
    * Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    if not condition.is_able_to_read_records(clinic):
        return

    # ============= Feedback =============

    if not clinic.current_patient.medical_records:
        tui.info(f"{clinic.current_patient.name} não possui anotações médicas.")
        return

    tui.bullet_list(
        f"Prontuário médico de {clinic.current_patient.name}:",
        clinic.current_patient.medical_records,
        additional_margin=12,
    )


def read_first_medical_annotation(clinic: Clinic):
    """Lê a primeira anotação do prontuário médico do paciente atual.

    Feedbacks
    ---------
    * Primeira anotação
    * Se não há anotações

    Warnings
    --------
    * Sessão não iniciada   : Propõe a iniciar
    * Sessão já finalizada
    * Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    if not condition.is_able_to_read_records(clinic):
        return

    # ============= Feedback =============

    if not clinic.current_patient.medical_records:
        tui.info(f"{clinic.current_patient.name} não possui anotações médicas.")
        return

    tui.info(
        [
            f"Primeira anotação médica de {clinic.current_patient.name}:",
            clinic.current_patient.medical_records[0],
        ]
    )


def read_last_medical_annotation(clinic: Clinic):
    """Lê a primeira anotação do prontuário médico do paciente atual.

    Feedbacks
    ---------
    * Primeira anotação
    * Se não há anotações

    Warnings
    --------
    * Sessão não iniciada   : Propõe a iniciar
    * Sessão já finalizada
    * Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    if not condition.is_able_to_read_records(clinic):
        return

    # ============= Feedback =============

    if not clinic.current_patient.medical_records:
        tui.info(f"{clinic.current_patient.name} não possui anotações médicas.")
        return

    tui.info(
        [
            f"Última anotação médica de {clinic.current_patient.name}:",
            clinic.current_patient.medical_records[-1],
        ]
    )
