import entities
from menus.use_cases import request, propose, warnings


def get_patient_use_case(clinic: entities.Clinic) -> entities.Patient | None:
    """Retorna um paciente
    
    Questions
    ---------
    CPF do paciente

    Warnings                    Proposes
    --------                    --------
    Paciente não registrado     Registrar paciente

    """
    cpf = request.patient_cpf()
    patient = clinic.patient_by_cpf(cpf)

    if not patient:
        warnings.patient_not_registered(cpf)
        if not propose.register_patient(clinic, cpf):
            return

        patient = clinic.patient_by_cpf(cpf)