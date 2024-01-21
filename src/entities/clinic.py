from .session import Session
from .patient import Patient


class Clinic:
    def __init__(self) -> None:
        self.current_session: Session | None = None
        self.current_patient: Patient | None = None
        self.waiting_queue: list[int] = []

        self.sessions: list[Session] = []
        self.patients: list[Patient] = []

        self.last_session_id = 0
        self.last_patient_id = 0

    def new_session_id(self):
        return self.last_session_id + 1

    def new_patient_id(self):
        return self.last_patient_id + 1

    def session_by_date(self, date: int) -> Session | None:
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
        return next(
            (patient for patient in self.patients if patient.cpf == cpf), None
        )

    def patient_by_id(self, uid: int) -> Patient | None:
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
