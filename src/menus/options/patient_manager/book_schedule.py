
from entities.clinic import ClinicModel
from tui.prompt import Prompt
from tui.warning import WarningScreen


def book_schedule(clinic: ClinicModel):
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
    """

    # Valida entradas
    try:
        patient_cpf = Prompt.get_cpf()
        session_date = Prompt.get_date()
    except ValueError as e:
        WarningScreen(e).render()
        return

    patient = clinic.patient_by_cpf(patient_cpf)
    session = clinic.session_by_date(session_date)

    # Valida registros
    if not patient:
        WarningScreen("Paciente não registrado.").render()
        return

    if not session:
        WarningScreen("Sessão não registrada.").render()
        return

    # Verifica o agendamento
    if session.uid in patient.scheduled_sessions:
        WarningScreen(
            f"Paciente {patient.name} já está "
            f"registrado para a sessão {session.formated_date}."
        ).render()
        return

    # Agenda sessão para paciente
    patient.scheduled_sessions.append(session.uid)
    WarningScreen("Paciente agendado com sucesso!").render()