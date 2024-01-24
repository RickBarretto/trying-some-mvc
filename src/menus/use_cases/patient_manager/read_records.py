import entity
from menus.use_cases.commons import condition
import tui

__all__ = [
    "read_first_medical_annotation",
    "read_full_medical_records",
    "read_last_medical_annotation",
]


def read_full_medical_records(clinic: entity.Clinic):
    """Lê o prontuário médico completo do paciente atual.

    Feedbacks
    ---------
    Listagem das anotações
    Se há anotações

    Warnings                        Proposes
    --------                        --------
    Sessão atual não iniciada       Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    is_able_to_read = condition.has_patient_being_attended and \
        condition.has_active_current_session_or_activate_it(clinic)
    
    if not is_able_to_read:
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


def read_first_medical_annotation(clinic: entity.Clinic):
    """Lê a primeira anotação do prontuário médico do paciente atual.

    Feedbacks
    ---------
    Primeira anotação
    Se não há anotações

    Warnings                        Proposes
    --------                        --------
    Sessão atual não iniciada       Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============
    
    is_able_to_read = condition.has_patient_being_attended and \
        condition.has_active_current_session_or_activate_it(clinic)
    
    if not is_able_to_read:
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


def read_last_medical_annotation(clinic: entity.Clinic):
    """Lê a primeira anotação do prontuário médico do paciente atual.

    Feedbacks
    ---------
    Primeira anotação
    Se não há anotações

    Warnings                        Proposes
    --------                        --------
    Sessão atual não iniciada       Iniciar sessão atual
    Sessão atual já finalizada
    Nenhum paciente sendo atendido

    """

    # ============= Verifica se é possível ler o prontuário =============

    is_able_to_read = condition.has_patient_being_attended and \
        condition.has_active_current_session_or_activate_it(clinic)
    
    if not is_able_to_read:
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
