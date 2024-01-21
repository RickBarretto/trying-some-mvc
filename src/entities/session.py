import enum
from dataclasses import dataclass


class SessionStatus(enum.Enum):
    UNBEGUN = 0
    BEGUN = 1
    FINISHED = 2

    def __str__(self) -> str:
        translate_table = {0: "não inicializado", 1: "inicializado", 2: "finalizado"}

        return translate_table[self.value]


@dataclass
class Session:
    uid: int
    date: str
    status: SessionStatus = SessionStatus.UNBEGUN

    def __str__(self) -> str:
        return f"{self.date}: {self.status} (ID: {self.uid})"
