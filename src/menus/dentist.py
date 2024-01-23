"""Define um Singleton para `reception`

Basicamente só pode existir uma única instância de `reception`,
e por consequência do controlador (model e view) que o mesmo possui.

Assim, é exposto uma única instância `reception`, 
ao invés da declaração de classe,
podendo assim ser usado por outros módulos.
"""


from menus.interface import MainMenu
from entities.clinic import Clinic

from .use_cases import current_session_manager
from .use_cases import patient_manager
from .use_cases import session_manager

import tui

# Todas as opções disponíveis para a dentist

def not_implemented(clinic: Clinic):
    tui.warn("Opção não implementada!")

options = [
    ("Procurar sessão por data.", session_manager.find),
    ("Iniciar sessão atual.", current_session_manager.start),
    ("Atender próximo paciente.", current_session_manager.attend_next_patient),
    ("Ler prontuário médico.", not_implemented),
    ("Ler primeira anotação do prontuário.", not_implemented),
    ("Ler última anotação do prontuário.", not_implemented),
    ("Fazer anotação no prontuário.", not_implemented),
]

reception = MainMenu(Clinic(), options)

__all__ = ["reception"]
