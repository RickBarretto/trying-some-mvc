from dataclasses import dataclass


@dataclass
class PatientModel:
    uid: int
    cpf: str
    name: str
    extra_info: list[str]

    def __post_init__(self):
        self.scheduled_sessions: list[int] = []

    def __str__(self) -> str:
        return f"{self.name} - CPF: {self.cpf} (ID: {self.uid})"
