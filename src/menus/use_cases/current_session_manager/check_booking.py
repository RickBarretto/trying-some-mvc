from entities.clinic import Clinic

from tui.prompt import Prompt
from tui.splash import SplashScreen
from tui.warning import WarningScreen


def check_current_booking(clinic: Clinic):
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
    """

    # Entrada do CPF
    try:
        cpf = Prompt.get_cpf()
    except ValueError as e:
        return WarningScreen(e).render()

    patient = clinic.patient_by_cpf(cpf)

    # Verifica se paciente existe no banco de dados
    if not patient:
        return WarningScreen("Paciente não registrado.").render()

    # Verifica se paciente está marcado para a sessão atual
    is_booked = clinic.current_session.uid in patient.scheduled_sessions

    # Imprime o feedback
    TEMPLATE_MESSAGE = "Paciente {} está marcado para a sessão atual."
    message = TEMPLATE_MESSAGE.format("" if is_booked else "não")

    SplashScreen([message]).render()
