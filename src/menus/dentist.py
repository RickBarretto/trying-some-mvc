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

# Todas as opções disponíveis para a dentist

__all__ = ["start"]

options = [
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

def current_patient(clinic: Clinic) -> str:
    if clinic.current_patient:
        return f"Paciente atual: {clinic.current_patient.name} - CPF {clinic.current_patient.cpf}"
    else:
        return "Nenhum paciente sendo atendido!"


def start(clinic: Clinic):
    dentist = MainMenu(clinic, options, status_func=current_patient)
    dentist.run()
