"""Define o menu da recepção"""


from entity.clinic import Clinic
import menus

from .use_cases import current_session_manager
from .use_cases import patient_manager
from .use_cases import session_manager


__all__ = ["start"]

# ============= Definição de variáveis internas =============

# Define as opções do menu da recepção

menu_options = [
    ("Registrar nova sessão", session_manager.register),
    ("Listar sessões registradas", session_manager.list_all),
    ("Procurar sessão por data", session_manager.find),
    ("Iniciar sessão atual", current_session_manager.start),
    ("Registrar novo paciente", patient_manager.register),
    ("Agendar sessão para paciente", patient_manager.book_schedule),
    ("Listar sessões agendadas para paciente", patient_manager.list_bookings),
    (
        "Verificar agendamento para sessão atual",
        current_session_manager.check_current_booking,
    ),
    (
        "Enviar paciente para fila de espera",
        current_session_manager.send_to_waiting_queue,
    ),
    ("Mostrar próximo paciente", current_session_manager.show_next_patient),
]


# ============= Definição de funções internas =============


def current_session_status(clinic: Clinic) -> str:
    """Função que atualiza o status que será impresso ao topo do menu."""
    if clinic.current_session:
        return f"Sessão atual: {clinic.current_session}"
    else:
        return "Sessão atual não configurada"


# ============= Definição de funções principais =============


def start(clinic: Clinic):
    """Função responsável por iniciar o menu da recepção."""
    menus.menu_loop(clinic, menu_options, status_func=current_session_status)
