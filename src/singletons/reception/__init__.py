from typing import Callable
from screen.main_menu import Controller, MainMenu
from entities import clinic

from singletons.options import current_session_manager
from singletons.options import patient_manager
from singletons.options import session_manager

__all__ = ["reception"]


class ReceptionMenu(MainMenu):
    pass


reception = ReceptionMenu(
    clinic.ClinicController(clinic.ClinicModel(), clinic.ClinicView()),
    [
        (session_manager.register_session, "Registrar nova sessão."),
        (session_manager.list_all, "Listar sessões registradas."),
        (session_manager.find, "Procurar sessão por data."),
        (current_session_manager.start_current_session, "Iniciar sessão atual."),
        (patient_manager.register, "Registrar novo paciente."),
        (patient_manager.book_schedule, "Agendar sessão para paciente."),
        (
            patient_manager.list_bookings,
            "Listar sessões agendadas para paciente.",
        ),
        (
            current_session_manager.check_current_booking,
            "Verificar agendamento para sessão atual.",
        ),
        (
            current_session_manager.send_to_waiting_queue,
            "Enviar paciente para fila de espera.",
        ),
        (current_session_manager.show_next_patient, "Mostrar próximo paciente."),
    ],
)
