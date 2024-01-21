from typing import Callable
from screen.main_menu import Controller, MainMenu
from entities import clinic


from .options import ReceptionOptions

from singletons.options import current_session_manager

__all__ = ["reception"]


class ReceptionMenu(MainMenu):
    pass


reception = ReceptionMenu(
    clinic.ClinicController(clinic.ClinicModel(), clinic.ClinicView()),
    [
        (ReceptionOptions.add_session, "Registrar nova sessão."),
        (ReceptionOptions.list_sessions, "Listar sessões registradas."),
        (ReceptionOptions.find_session, "Procurar sessão por data."),
        (ReceptionOptions.start_session, "Iniciar sessão atual."),
        (ReceptionOptions.register_patient, "Registrar novo paciente."),
        (ReceptionOptions.book_schedule, "Agendar sessão para paciente."),
        (
            ReceptionOptions.list_patient_bookings,
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
