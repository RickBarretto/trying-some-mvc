from dataclasses import dataclass


@dataclass
class Patient:
    """Define o modelo do Paciente
    
    Attributes
    ----------
    uid: int
        O ID do paciente (``uid`` significa 'unique id').
    cpf: str
        O CPF do paciente.
    name: str
        O Nome do paciente.
    extra_info: list[str]
        Informações extras do paciente.

    scheduled_sessions: list[int]
        Contém os IDs das sessões agendadas pelo paciente.
    medical_records: list[str]
        Contém o prontuário médico do paciente. 
        Que nada mais é que uma lista de anotações médicas.

    """
    uid: int
    cpf: str
    name: str
    extra_info: list[str]

    def __post_init__(self):
        # Como no Python 3.10 é impossível usar um valor padrão 
        # sem usar o default_factory,
        # decidi usar o post-init.
        # Para mais informações leia: https://docs.python.org/3.10/library/dataclasses.html

        self.scheduled_sessions: list[int] = []
        self.medical_records: list[str] = []

    def __str__(self) -> str:
        """Dunder método que converte a classe atual em string.
        
        Example
        -------
        >>> p = Patient(1, '000.000.000-00', 'Meu Nome', [])
        >>> str(p)
        Meu Nome - CPF: 000.000.000-00 (ID: 1)
        """
        return f"{self.name} - CPF: {self.cpf} (ID: {self.uid})"
