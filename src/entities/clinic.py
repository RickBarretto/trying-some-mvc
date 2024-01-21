from .session import SessionModel
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

    def new_session_id(self):
        return self.last_session_id + 1

    def new_patient_id(self):
        return self.last_patient_id + 1

    def update_current_session(self, date: int):
        if session := self.session_by_date(date):
            self.current_session = session
            return

        self.current_session = self.register_session(date)

    def session_by_date(self, date: int) -> SessionModel | None:
        """Retorna uma sessão existente na data ``date``.

        Retornará ``None`` caso a sessão não exista.
        """
        return next(
            (session for session in self.sessions if session.date == date), None
        )

    def patient_by_cpf(self, cpf: str) -> PatientModel | None:
        """Procura paciente pelo ``cpf``.

        Se não encontrado, retorna ``None``.
        """
        return next(
            (patient for patient in self.patients if patient.cpf == cpf), None
        )

    def patient_by_id(self, uid: int) -> PatientModel | None:
        """Procura paciente pelo ``uid``.

        Se não encontrado, retorna ``None``.
        """
        return next(
            (patient for patient in self.patients if patient.uid == uid), None
        )


# I'm here as a reference
# TODO: Implement or delete me!
#
# def attend_next_patient(self) -> bool:
#     """Atende o próximo paciente da fila de espera.
# 
#     Assertions
#     ----------
#     `waiting_queue` não pode estar vazia
#     """
#     assert self.waiting_queue
# 
#     patient_id = self.waiting_queue.pop(0)
#     self.current_patient = self.patient_by_id(patient_id)
