"""Definem as condições comuns das regras de negócio

Algumas dessas condições incluem propostas ao usuário para contornar
o problema lidado.

See Also
--------
``menus.use_cases.proposes`` para mais informações dessas propostas.
"""

from entities.clinic import Clinic
from entities.session import SessionStatus

from menus.use_cases import propose, warnings

import tui


def is_able_to_read_records(clinic: Clinic) -> bool:
    """Retorna se o médico é capaz de ler o prontuário.
    
    Um médico é capaz de ler o prontuário se e somente se:
        1. A sessão já foi iniciada
        2. Tem um paciente sendo atendido.
    """
    return has_patient_being_attended(clinic) and has_active_current_session_or_activate_it(clinic)


def has_active_current_session_or_activate_it(clinic: Clinic) -> bool:
    """Retorna se a sessão atual está ativa ou não, ou propõe a ativar.
    
    Warnings                        Proposes
    --------                        --------
    Sessão nunca fora iniciada      Iniciar sessão
    Sessão já finalizada

    """

    # Caso a sessão não tenha sido iniciada ainda, propõe iniciá-la.
    if clinic.current_session.status == SessionStatus.UNBEGUN:
        warnings.session_has_never_started(clinic.current_session)
        if not propose.start_current_session(clinic):
            return False

    # Caso a sessão esteja finalizada, a leitura não pode ser mais feita.
    if clinic.current_session.status == SessionStatus.FINISHED:
        warnings.session_has_already_been_finished(clinic.current_session)
        return False

    return True


def has_patient_being_attended(clinic: Clinic) -> bool:
    """Retorna se há um paciente sendo atendido.
    
    Warnings
    --------
    Nenhum paciente sendo atendido
    """
    if not (res := clinic.current_patient):
        tui.warn("Nenhum paciente sendo atendido!")
    return bool(res)
