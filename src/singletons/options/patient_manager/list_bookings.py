from entities.clinic import ClinicController
from screen.list import ListScreen
from screen.prompt import Prompt
from screen.warning import WarningScreen


def list_patient_bookings(clinic: ClinicController):
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

    patient = clinic.find_patient(cpf)

    # Verifica registro
    if patient is None:
        WarningScreen("Paciente não registrado.").render()
        return

    # Lista sessões agendadas
    booked_sessions = clinic.get_patient_bookings(patient)
    data = booked_sessions if booked_sessions else ["Nenhuma sessão agendada"]

    ListScreen("Sessões agendadas", data).render()
