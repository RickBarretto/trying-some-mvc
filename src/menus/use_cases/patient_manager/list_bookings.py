from entities.clinic import Clinic
from tui.list import ListScreen
from tui.prompt import Prompt
from tui.warning import WarningScreen

from menus.use_cases import status


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

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Valida entrada
    try:
        cpf = Prompt.get_cpf()
    except ValueError as e:
        WarningScreen(e).render()
        return status.MayBeRepeated

    patient = clinic.patient_by_cpf(cpf)

    # Verifica registro

    # TODO: perguntar se deseja registrar
    if patient is None:
        WarningScreen("Paciente não registrado.").render()
        return status.Ok

    # Lista sessões agendadas

    sessions_ids = patient.scheduled_sessions
    sessions = [session for session in clinic.sessions if session.uid in sessions_ids]

    data = sessions if sessions else ["Nenhuma sessão agendada"]

    ListScreen("Sessões agendadas", data).render()
    return status.Ok
