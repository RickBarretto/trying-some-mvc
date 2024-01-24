"""Define um Singleton para `reception`

Basicamente só pode existir uma única instância de `reception`,
e por consequência do controlador (model e view) que o mesmo possui.

Assim, é exposto uma única instância `reception`, 
ao invés da declaração de classe,
podendo assim ser usado por outros módulos.
"""


from menus.interface import main_menu_loop
from entities.clinic import Clinic

from .use_cases import current_session_manager
from .use_cases import patient_manager
from .use_cases import session_manager

__all__ = ["start"]

# ============= Definição de variáveis internas =============

# Define as opções do menu do dentista
menu_options = [
    ("Procurar sessão por data", session_manager.find),
    ("Iniciar sessão atual", current_session_manager.start),
    ("Atender próximo paciente", current_session_manager.attend_next_patient),
    ("Ler prontuário médico", patient_manager.read_full_medical_records),
    (
        "Ler primeira anotação do prontuário",
        patient_manager.read_first_medical_annotation,
    ),
    (
        "Ler última anotação do prontuário",
        patient_manager.read_last_medical_annotation,
    ),
    ("Fazer anotação no prontuário", patient_manager.annotate_medical_records),
]


# ============= Definição de funções internas =============


def current_patient_status(clinic: Clinic) -> str:
    """Função que atualiza o status que será impresso ao topo do menu."""

    if clinic.current_patient:
        return f"Paciente atual: {clinic.current_patient}"
    else:
        return "Nenhum paciente sendo atendido!"


# ============= Definição de funções principais =============


def start(clinic: Clinic):
    """Função responsável por iniciar o menu do dentista."""
    main_menu_loop(clinic, menu_options, status_func=current_patient_status)
