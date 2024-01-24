import entities
from menus.use_cases import request, propose, warnings


def get_patient(clinic: entities.Clinic) -> entities.Patient | None:
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

    return clinic.patient_by_cpf(cpf)


def get_sesssion(clinic: entities.Clinic) -> entities.Clinic | None:
    """Retorna um paciente
    
    Questions
    ---------
    Data da sessão

    Warnings                    Proposes
    --------                    --------
    Sessão não registrada       Registrar sessão

    """
    session_date = request.session_date()
    session = clinic.session_by_date(session_date)

    if not session:
        warnings.session_not_registered(session_date)
        if propose.register_session(clinic, session_date):
            return

    return clinic.session_by_date(session_date)