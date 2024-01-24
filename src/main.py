"""Módulo principal

Para rodar a aplicação execute

        $ py src/main.py        # windows
        $ python src/main.py    # linux
"""

from entities.clinic import Clinic
from menus.application import start_application


if __name__ == "__main__":
    clinic_singleton = Clinic()
    start_application(clinic_singleton)
