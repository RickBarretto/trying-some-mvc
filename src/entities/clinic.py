from .session import SessionModel, SessionStatus
from .patient import PatientModel


class ClinicModel:
    def __init__(self) -> None:
        self.current_session: SessionModel | None = None
        self.waiting_queue: list[int] = []

        self.sessions: list[SessionModel] = []
        self.patients: list[PatientModel] = []

        self.last_session_id = 0
        self.last_patient_id = 0

    @property
    def current_patient_id(self) -> int | None:
        if self.waiting_queue:
            return self.waiting_queue[0]

        return None

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

    def register_session(self, date: int) -> SessionModel | None:
        """Adiciona nova sessão, retornando a sessão criada em caso de sucesso.

        Se a sessão já existe, será retornado ``None``.
        """

        # Verifica se sessão já está registrado
        if self.find_session(date):
            return None

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
        """Retorna uma sessão existente na data ``date``."""

        for session in self.model.sessions:
            if session.date == date:
                return session

        return None

    def start_session(self) -> bool:
        if self.model.current_session.status != SessionStatus.UNBEGUN:
            return False

        self.model.current_session.status = SessionStatus.BEGUN
        return True

    def register_patient(
        self, cpf: str, name: str, extra_info: list[str]
    ) -> PatientModel:
        """Adiciona nova paciente, retornando o paciente criado.

        Se o paciente já existe, será retornado ``None``.
        """

        # Verifica se sessão já está registrado
        for patient in self.model.patients:
            if patient.cpf == cpf:
                return None

        # Declaração de variáveis
        new_id: int = self.model.new_patient_id
        patient: PatientModel = PatientModel(
            uid=new_id, cpf=cpf, name=name, extra_info=extra_info
        )

        # Registro da nova sessão
        self.model.patients.append(patient)
        self.model.last_patient_id = new_id

        return patient

    def find_patient(self, cpf: str) -> PatientModel | None:
        """Procura paciente pelo ``cpf``.

        Se não encontrado, retorna ``None``.
        """

        for patient in self.model.patients:
            if patient.cpf == cpf:
                return patient

        return None

    def book_schedule(self, patient: PatientModel, session: SessionModel) -> bool:
        """Agenda paciente para uma sessão, e retorna o status do agendamento.

        Retorna ``False`` caso a sessão já tenha sido registrada.
        """
        if session.uid in patient.scheduled_sessions:
            return False

        patient.scheduled_sessions.append(session.uid)
        return True

    def get_patient_bookings(self, patient: PatientModel) -> list[str]:
        sessions_ids = patient.scheduled_sessions
        sessions = [
            session for session in self.model.sessions if session.uid in sessions_ids
        ]

        return self.view.display_sessions(sessions)

    def push_to_queue(self, cpf: str):
        if not (patient := self.find_patient(cpf)):
            return False

        self.model.waiting_queue.append(patient.uid)
        return True

    def shift_queue(self) -> bool:
        if len(self.model.waiting_queue) < 2:
            return False

        self.model.waiting_queue.pop(0)
        return True
