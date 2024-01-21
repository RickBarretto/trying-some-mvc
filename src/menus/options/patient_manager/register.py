from entities.clinic import ClinicController
from entities.patient import PatientModel
from tui.prompt import Prompt
from tui.warning import WarningScreen


def register(clinic: ClinicController):
    """Registra paciente no banco de dados.

    Questions
    ---------
    * CPF do paciente
    * Nome do paciente
    * Informações extras

    Feedbacks
    ---------
    * Registro foi um sucesso

    Warnings
    --------
    * Formato de CPF inválido
    * TODO: Nome não deve conter números ou símbolos
    * TODO: Nome deve conter pelo menos nome e sobrenome
    * Paciente já registrado
    """

    # Valida entradas
    try:
        cpf: str = Prompt.get_cpf()
        name: str = Prompt.prompt("Insira o nome do paciente.")
        extra: str = Prompt.multiline("Insira informações extra.")
    except ValueError as e:
        WarningScreen(e).render()
        return

    # Verifica se paciente já está registrado
    if clinic.patient_by_cpf(cpf):
        WarningScreen("Paciente já foi registrado.").render()
        return

    # Criação do paciente
    new_id: int = clinic.model.new_patient_id
    patient: PatientModel = PatientModel(
        uid=new_id, 
        cpf=cpf, 
        name=name, 
        extra_info=extra
    )

    # Registro do paciente
    clinic.model.patients.append(patient)
    clinic.model.last_patient_id_id = new_id

    WarningScreen(f"{patient.name} registrado com sucesso!").render()