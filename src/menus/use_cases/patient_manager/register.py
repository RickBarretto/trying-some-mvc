from entities.clinic import Clinic
from entities.patient import Patient

import tui

from menus.use_cases import request


def register(clinic: Clinic, patient_cpf: str | None = None):
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

    # ============= Verifica registro de paciente =============

    if not patient_cpf:
        patient_cpf = request.patient_cpf()

    if clinic.patient_by_cpf(patient_cpf):
        tui.warn("Paciente já foi registrado.")
        return

    # ============= Adiciona dados extras =============

    patient_name: str = tui.prompt("Insira o nome do paciente.")
    extra_information: str = tui.multiline("Insira informações extra.")

    # ============= Registra paciente =============

    patient = register_patient(clinic, patient_cpf, patient_name, extra_information)
    tui.info(f"{patient.name} registrado com sucesso!")


def register_patient(clinic: Clinic, cpf: str, name: str, extra: list[str]) -> Patient:
    new_id: int = clinic.new_patient_id()
    patient = Patient(uid=new_id, cpf=cpf, name=name, extra_info=extra)

    clinic.patients.append(patient)
    clinic.last_patient_id_id = new_id

    return patient
