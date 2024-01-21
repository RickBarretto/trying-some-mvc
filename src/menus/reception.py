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

# Todas as opções disponíveis para a recepção

options = [
    (session_manager.register, "Registrar nova sessão."),
    (session_manager.list_all, "Listar sessões registradas."),
    (session_manager.find, "Procurar sessão por data."),
    (current_session_manager.start_current_session, "Iniciar sessão atual."),
    (patient_manager.register, "Registrar novo paciente."),
    (patient_manager.book_schedule, "Agendar sessão para paciente."),
    (patient_manager.list_bookings,"Listar sessões agendadas para paciente.",),
    (current_session_manager.check_current_booking, "Verificar agendamento para sessão atual.",),
    (current_session_manager.send_to_waiting_queue,"Enviar paciente para fila de espera.",),
    (current_session_manager.show_next_patient, "Mostrar próximo paciente."),
]

reception = MainMenu(Clinic(), options)

__all__ = ["reception"]
