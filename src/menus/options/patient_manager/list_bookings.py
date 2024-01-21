from entities.clinic import Clinic
from tui.list import ListScreen
from tui.prompt import Prompt
from tui.warning import WarningScreen


def list_bookings(clinic: Clinic):
    """Lista os agendamentos de um paciente.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Lista de agendamentos
    * Nenhum agendamento

    Warnings
    --------
    * Formato de CPF inválido
    * Paciente não registrado
    """

    # Valida entrada
    try:
        cpf = Prompt.get_cpf()
    except ValueError as e:
        WarningScreen(e).render()
        return

    patient = clinic.patient_by_cpf(cpf)

    # Verifica registro
    if patient is None:
        WarningScreen("Paciente não registrado.").render()
        return

    # Lista sessões agendadas

    sessions_ids = patient.scheduled_sessions
    sessions = [
        session for session in clinic.sessions if session.uid in sessions_ids
    ]

    data = sessions if sessions else ["Nenhuma sessão agendada"]

    ListScreen("Sessões agendadas", data).render()
