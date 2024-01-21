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
    def display_sessions(self, sessions: list[SessionModel]) -> list[str]:
        return [self.format_session(session) for session in sessions]

    def format_session(self, session: SessionModel) -> str:
        uid = session.uid
        date = session.formated_date
        status = session.status

        return f"{date}: {status} (ID: {uid})"

    def format_patient(self, patient: PatientModel) -> str:
        uid = patient.uid
        cpf = patient.cpf
        name = patient.name

        return f"{name} - CPF: {cpf} (ID: {uid})"


class ClinicController:
    def __init__(self, model: ClinicModel, view: ClinicView) -> None:
        self.model = model
        self.view = view

    def update_current_session(self, date: int):
        if session := self.find_session(date):
            self.model.current_session = session
            return

        self.model.current_session = self.register_session(date)

    def register_session(self, date: int) -> SessionModel:
        """Cria e registra nova sessão a retornando.

        Arguments
        ---------
        date: str
            Data da sessão

        Assertions
        ----------
        * `session` não pode já estar registrado em `model.sessions`
        """
        assert self.find_session(date) is None

        # Declaração de variáveis
        new_id: int = self.model.new_session_id
        session: SessionModel = SessionModel(uid=new_id, date=date)

        # Registro da nova sessão
        self.model.sessions.append(session)
        self.model.last_session_id = new_id

        return session

    def get_sessions(self) -> list[str]:
        """Retorna uma lista com dados formatados das sessões disponíveis"""
        sessions = self.model.sessions
        formated_sessions = self.view.display_sessions(sessions)
        return formated_sessions

    def find_session(self, date: int) -> SessionModel | None:
        """Retorna uma sessão existente na data ``date``.

        Retornará ``None`` caso a sessão não exista.
        """
        return next(
            (session for session in self.model.sessions if session.date == date), None
        )

    def start_session(self) -> bool:
        if self.model.current_session.status != SessionStatus.UNBEGUN:
            return False

        self.model.current_session.status = SessionStatus.BEGUN
        return True

    def register_patient(
        self, cpf: str, name: str, extra_info: list[str]
    ) -> PatientModel:
        """Cria e registra novo paciente o retornando.

        Arguments
        ---------
        cpf: str
            CPF do paciente
        name: str
            Nome do paciente
        extra_info: list[str]
            Informações abirtrárias sobre o paciente

        Assertions
        ----------
        * `patient` não pode já estar registrado em `model.patients`
        """
        assert self.find_patient(cpf) is None

        # Criação do novo paciente
        new_id: int = self.model.new_patient_id
        patient: PatientModel = PatientModel(
            uid=new_id, cpf=cpf, name=name, extra_info=extra_info
        )

        # Registro do novo paciente
        self.model.patients.append(patient)
        self.model.last_patient_id = new_id

        return patient

    def find_patient(self, cpf: str) -> PatientModel | None:
        """Procura paciente pelo ``cpf``.

        Se não encontrado, retorna ``None``.
        """
        return next(
            (patient for patient in self.model.patiens if patient.cpf == cpf), None
        )

    def get_patient(self, uid: int) -> PatientModel | None:
        """Procura paciente pelo ``uid``.

        Se não encontrado, retorna ``None``.
        """
        return next(
            (patient for patient in self.model.patiens if patient.uid == uid), None
        )

    def book_schedule(self, patient: PatientModel, session: SessionModel) -> None:
        """Agenda paciente para uma sessão.

        Assertions
        ----------
        * `patient` deve estar registrado
        * `session` deve estar registrada
        * `session.uid` não pode estar agendada em `patient.scheduled_sessions`
        """
        assert patient in self.model.patients
        assert session in self.model.sessions
        assert session.uid not in patient.scheduled_sessions

        patient.scheduled_sessions.append(session.uid)

    def get_patient_bookings(self, patient: PatientModel) -> list[str]:
        """Retorna uma lista com os agendamentos feito pelo paciente."""
        sessions_ids = patient.scheduled_sessions
        sessions = [
            session for session in self.model.sessions if session.uid in sessions_ids
        ]

        return self.view.display_sessions(sessions)

    def push_to_waiting_queue(self, patient: PatientModel) -> None:
        """Coloca paciente na fila de espera.

        Assertions
        ----------
        `patiend.uid` não pode já estar dentro de `model.waiting_queue`
        """
        assert patient.uid not in self.model.waiting_queue
        self.model.waiting_queue.append(patient.uid)

    def attend_next_patient(self) -> bool:
        """Atende o próximo paciente da fila de espera.

        Assertions
        ----------
        `model.waiting_queue` não pode estar vazia
        """
        assert self.model.waiting_queue

        patient_id = self.model.waiting_queue.pop(0)
        self.current_patient = self.get_patient(patient_id)
