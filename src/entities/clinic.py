from .session import SessionModel, SessionStatus
from .patient import PatientModel


class ClinicModel:
    def __init__(self) -> None:
        self.current_session: SessionModel | None = None
        self.current_patient: PatientModel | None = None
        self.waiting_queue: list[int] = []

        self.sessions: list[SessionModel] = []
        self.patients: list[PatientModel] = []

        self.last_session_id = 0
        self.last_patient_id = 0

    @property
    def new_session_id(self):
        return self.last_session_id + 1

    @property
    def new_patient_id(self):
        return self.last_patient_id + 1


class ClinicView:
    pass


class ClinicController:
    def __init__(self, model: ClinicModel, view: ClinicView) -> None:
        self.model = model
        self.view = view

    def update_current_session(self, date: int):
        if session := self.session_by_date(date):
            self.model.current_session = session
            return

        self.model.current_session = self.register_session(date)

    def session_by_date(self, date: int) -> SessionModel | None:
        """Retorna uma sessão existente na data ``date``.

        Retornará ``None`` caso a sessão não exista.
        """
        return next(
            (session for session in self.model.sessions if session.date == date), None
        )

    def patient_by_cpf(self, cpf: str) -> PatientModel | None:
        """Procura paciente pelo ``cpf``.

        Se não encontrado, retorna ``None``.
        """
        return next(
            (patient for patient in self.model.patiens if patient.cpf == cpf), None
        )

    def patient_by_id(self, uid: int) -> PatientModel | None:
        """Procura paciente pelo ``uid``.

        Se não encontrado, retorna ``None``.
        """
        return next(
            (patient for patient in self.model.patiens if patient.uid == uid), None
        )

    def attend_next_patient(self) -> bool:
        """Atende o próximo paciente da fila de espera.

        Assertions
        ----------
        `model.waiting_queue` não pode estar vazia
        """
        assert self.model.waiting_queue

        patient_id = self.model.waiting_queue.pop(0)
        self.current_patient = self.patient_by_id(patient_id)
