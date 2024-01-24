import enum
from dataclasses import dataclass


class SessionStatus(enum.Enum):
    """Enumeração para o status de ``Session``

    Uma sessão pode estar em três estados:
    * Não inicializada
    * Inicializada
    * Finalizada

    Note
    ----
    A escolha de ``Enum`` foi devido a manter as
    boas práticas quanto mudança de estados.
    """

    UNBEGUN = 0
    BEGUN = 1
    FINISHED = 2

    def __str__(self) -> str:
        """Converte os valores da enumeração para informações em português."""
        translate_table = {0: "não inicializado", 1: "inicializado", 2: "finalizado"}

        return translate_table[self.value]


@dataclass
class Session:
    """Definição de uma sessão

    Attributes
    ----------
    uid: int
        ID da sessão (``uid`` significa 'unique id').
    date: str
        Data da sessão.
    status: SessionStatus = SessionStatus.UNBEGUN
        Status da sessão. Iniciado como não-inicializado.
    """

    uid: int
    date: str
    status: SessionStatus = SessionStatus.UNBEGUN

    def __str__(self) -> str:
        """Converte a classe para uma string.

        Example
        -------
        >>> s = Session(1, "01/01/2024")
        >>> str(s)
        01/01/2024: não inicializado (ID: 1)
        """
        return f"{self.date}: {self.status} (ID: {self.uid})"
