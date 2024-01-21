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
class SessionModel:
    uid: int
    date: int
    status: SessionStatus = SessionStatus.UNBEGUN

    @property
    def formated_date(self) -> str:
        date_str = str(self.date)

        day = date_str[-2:]
        month = date_str[-4:-2]
        year = date_str[:-4]

        return f"{day}/{month}/{year}"

    def __str__(self) -> str:
        return f"{self.date}: {self.status} (ID: {self.uid})"