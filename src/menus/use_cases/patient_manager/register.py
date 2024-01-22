from entities.clinic import Clinic
from entities.patient import Patient
from tui import prompt

import tui

from menus.use_cases import status


def register(clinic: Clinic) -> bool:
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

    Return
    ------
    bool:
        Retorna o status da função, que pode ser `status.Ok` (`True`)
        ou `status.MayBeRepeated` (`False`).
    """

    # Valida entradas
    try:
        cpf: str = prompt.get_cpf()
        name: str = prompt.prompt("Insira o nome do paciente.")
        extra: str = prompt.multiline("Insira informações extra.")
    except ValueError as e:
        tui.warn(e)
        return status.MayBeRepeated

    # Verifica se paciente já está registrado
    if clinic.patient_by_cpf(cpf):
        tui.warn("Paciente já foi registrado.")
        return status.Ok

    # Criação do paciente
    new_id: int = clinic.new_patient_id()
    patient: Patient = Patient(uid=new_id, cpf=cpf, name=name, extra_info=extra)

    # Registro do paciente
    clinic.patients.append(patient)
    clinic.last_patient_id_id = new_id

    tui.warn(f"{patient.name} registrado com sucesso!")
    return status.Ok
