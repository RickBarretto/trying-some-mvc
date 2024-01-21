

from unittest import TestCase
from unittest.mock import patch
from singletons.startup import startup

def fake_input(msg: str):
    yield "1"
    yield "10/12/2002"
    yield ""

    # Registrar pacientes

    yield "5"
    yield "000.000.000-00"
    yield "Rick"
    yield ""
    yield ""
    
    yield "5"
    yield "000.000.000-01"
    yield "Rick 2"
    yield ""
    yield ""

    # Agendar pacientes

    yield "6"
    yield "000.000.000-00"
    yield "10/12/2002"
    yield ""
    
    yield "6"
    yield "000.000.000-01"
    yield "10/12/2002"
    yield ""
    yield ""

    # Enfileirar

    yield "9"
    yield "000.000.000-00"
    yield ""
    
    yield "9"
    yield "000.000.000-01"
    yield ""

    # Resultado

    yield "10"


__builtins__.input = fake_input

if __name__ == "__main__":
    startup.run()
