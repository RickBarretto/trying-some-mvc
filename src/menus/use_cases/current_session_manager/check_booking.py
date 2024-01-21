from entities.clinic import Clinic

from tui.prompt import Prompt
from tui.splash import SplashScreen
from tui.warning import WarningScreen

from menus.use_cases import status


def check_current_booking(clinic: Clinic) -> bool:
    """Verifica se paciente está agendado para a sessão atual.

    Questions
    ---------
    * CPF do paciente

    Feedbacks
    ---------
    * Status do agendamento

    Warnings
    --------
    * Paciente não registrado

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Entrada do CPF
    try:
        cpf = Prompt.get_cpf()
    except ValueError as e:
        WarningScreen(e).render()
        return status.MayBeRepeated

    patient = clinic.patient_by_cpf(cpf)

    # Verifica se paciente existe no banco de dados

    # TODO: registrar paciente caso necessário
    if not patient:
        WarningScreen("Paciente não registrado.").render()
        return status.Ok

    # Verifica se paciente está marcado para a sessão atual
    is_booked = clinic.current_session.uid in patient.scheduled_sessions

    # Imprime o feedback
    
    TEMPLATE_MESSAGE = "Paciente {}{}está marcado para a sessão atual."
    message = TEMPLATE_MESSAGE.format(patient.name, " " if is_booked else " não ")

    SplashScreen([message]).render()
    return status.Ok
