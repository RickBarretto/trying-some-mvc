"""Define um Singleton para `reception`

Basicamente só pode existir uma única instância de `reception`,
e por consequência do controlador (model e view) que o mesmo possui.

Assim, é exposto uma única instância `reception`, 
ao invés da declaração de classe,
podendo assim ser usado por outros módulos.
"""

from entities.clinic import Clinic
from menus.interface import MainMenu
from .use_cases import current_session_manager
from .use_cases import patient_manager
from .use_cases import session_manager

# Todas as opções disponíveis para a recepção

__all__ = ["start"]

options = [
    ("Registrar nova sessão.", session_manager.register),
    ("Listar sessões registradas.", session_manager.list_all),
    ("Procurar sessão por data.", session_manager.find),
    ("Iniciar sessão atual.", current_session_manager.start),
    ("Registrar novo paciente.", patient_manager.register),
    ("Agendar sessão para paciente.", patient_manager.book_schedule),
    ("Listar sessões agendadas para paciente.", patient_manager.list_bookings),
    (
        "Verificar agendamento para sessão atual.",
        current_session_manager.check_current_booking,
    ),
    (
        "Enviar paciente para fila de espera.",
        current_session_manager.send_to_waiting_queue,
    ),
    ("Mostrar próximo paciente.", current_session_manager.show_next_patient),
]

def start(clinic: Clinic):
    reception = MainMenu(clinic, options)
    reception.run()