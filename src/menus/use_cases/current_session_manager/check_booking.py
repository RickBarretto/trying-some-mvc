from entities.clinic import Clinic
import tui
from menus.use_cases import proposes, request, status


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
    * Paciente não registrado   : Propõe o registrar.

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`True`).
    """

    # Entrada do CPF
    cpf = request.patient_cpf()

    # Verifica se paciente existe no banco de dados

    if not (patient := clinic.patient_by_cpf(cpf)):
        tui.warn("Paciente não registrado.")

        if proposes.register_patient(clinic, cpf):
            patient = clinic.patient_by_cpf(cpf)
        else:
            return status.Ok

    # Verifica se paciente está marcado para a sessão atual
    is_booked = clinic.current_session.uid in patient.scheduled_sessions

    # Imprime o feedback

    TEMPLATE_MESSAGE = "Paciente {}{}está marcado para a sessão atual."
    message = TEMPLATE_MESSAGE.format(patient.name, " " if is_booked else " não ")

    tui.info(message)

    if not is_booked:
        if not proposes.book_session(clinic, patient, clinic.current_session):
            return status.Ok

    proposes.send_patient_to_waiting_queue(clinic, patient)
