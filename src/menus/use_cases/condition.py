

from entities.clinic import Clinic
from entities.session import SessionStatus

from menus.use_cases import propose, warnings

import tui

def is_able_to_read_records(clinic: Clinic) -> bool:
    has_patient_being_attended(clinic) and has_active_current_session(clinic)

def has_active_current_session(clinic: Clinic) -> bool:
    if clinic.current_session.status == SessionStatus.UNBEGUN:
        warnings.session_has_never_started(clinic.current_session)
        if not propose.start_current_session(clinic):
            return False

    if clinic.current_session.status == SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return False
    
    return True

def has_patient_being_attended(clinic: Clinic) -> bool:
    if not (res := clinic.current_patient):
        tui.warn("Nenhum paciente sendo atendido.")
    return res
