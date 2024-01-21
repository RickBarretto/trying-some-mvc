from entities.clinic import Clinic
from tui.prompt import Prompt
from tui.warning import WarningScreen

from menus.use_cases import status


def book_schedule(clinic: Clinic) -> bool:
    """Agenda uma sessão para um paciente.

    Questions
    ---------
    * CPF do paciente
    * Data da sessão

    Feedbacks
    ---------
    * Status do agendamento

    Warnings
    --------
    * Formato de data inválido
    * Formato de CPF inválido
    * Paciente não registrado
    * Sessão não registrada
    * Sessão já finalizada
    * Paciente já estava agendado

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Valida entradas
    try:
        patient_cpf = Prompt.get_cpf()
        session_date = Prompt.get_date()
    except ValueError as e:
        WarningScreen(e).render()
        return status.MayBeRepeated

    patient = clinic.patient_by_cpf(patient_cpf)
    session = clinic.session_by_date(session_date)

    # Valida registros

    # TODO: perguntar se deseja registar
    if not patient:
        WarningScreen("Paciente não registrado.").render()
        return status.Ok

    # TODO: perguntar se deseja registar
    if not session:
        WarningScreen("Sessão não registrada.").render()
        return status.Ok

    # Verifica o agendamento
    if session.uid in patient.scheduled_sessions:
        WarningScreen(
            f"Paciente {patient.name} já está "
            f"registrado para a sessão {session.date}."
        ).render()
        return status.Ok

    # Agenda sessão para paciente
    patient.scheduled_sessions.append(session.uid)

    # TODO: usar InfoScreen
    WarningScreen(f"{patient.name} agendado para o dia {session.date}!").render()
    return status.Ok
