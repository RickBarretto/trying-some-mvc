from .session import Session
from .patient import Patient


class Clinic:
    """Define o modelo da Clínica

    Attributes
    ----------
    current_session: Session | None = None
        Define a sessão atual, inicialmente sendo None
    current_patient: Patient | None = None
        Define o paciente atual, inicialmente sendo None
    waiting_queue: list[int]
        A fila de espera é uma lista com os IDs dos pacientes (``Patient.uid``)

    sessions: list[Session]
        Lista de sessões registradas no banco de dados
    patients: list[Patient]
        Lista de pacientes registrados no banco de dados

    last_session_id: int = 0
    last_patient_id: int = 0
        Armazena o último ID gerado para o banco de dados
        das sessões e pacientes, respectivamente

    """

    def __init__(self) -> None:
        self.current_session: Session | None = None
        self.current_patient: Patient | None = None
        self.waiting_queue: list[int] = []

        self.sessions: list[Session] = []
        self.patients: list[Patient] = []

        self.last_session_id = 0
        self.last_patient_id = 0

    def new_session_id(self):
        """Gera um novo ID para sessão"""
        return self.last_session_id + 1

    def new_patient_id(self):
        """Gera um novo ID para paciente"""
        return self.last_patient_id + 1

    def session_by_date(self, date: str) -> Session | None:
        """Retorna uma sessão existente na data ``date``.

        Retornará ``None`` caso a sessão não exista.
        """
        return next(
            (session for session in self.sessions if session.date == date), None
        )

    def patient_by_cpf(self, cpf: str) -> Patient | None:
        """Procura paciente pelo ``cpf``.

        Se não encontrado, retorna ``None``.
        """
        return next((patient for patient in self.patients if patient.cpf == cpf), None)

    def patient_by_id(self, uid: int) -> Patient | None:
        """Procura paciente pelo ``uid``.

        Se não encontrado, retorna ``None``.
        """
        return next((patient for patient in self.patients if patient.uid == uid), None)
