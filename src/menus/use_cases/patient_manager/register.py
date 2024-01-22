from entities.clinic import Clinic
from entities.patient import Patient

import tui

from menus.use_cases import request


def register(clinic: Clinic, patient_cpf: str | None = None) -> bool:
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
    if not patient_cpf:
        patient_cpf = request.patient_cpf()

    # Verifica se paciente já é registrado
    if clinic.patient_by_cpf(patient_cpf):
        tui.warn("Paciente já foi registrado.")
        return 

    # Adiciona outros dados do paciente
    patient_name: str = tui.prompt("Insira o nome do paciente.")
    extra_information: str = tui.multiline("Insira informações extra.")

    # Criação do paciente
    new_id: int = clinic.new_patient_id()
    patient: Patient = Patient(
        uid=new_id, cpf=patient_cpf, name=patient_name, extra_info=extra_information
    )

    # Registro do paciente
    clinic.patients.append(patient)
    clinic.last_patient_id_id = new_id

    tui.info(f"{patient.name} registrado com sucesso!")
