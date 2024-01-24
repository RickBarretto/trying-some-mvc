"""Módulo principal

Para rodar a aplicação execute

        $ py src/main.py        # windows
        $ python src/main.py    # linux
"""

import entity
from menus.application import start_application


if __name__ == "__main__":
    clinic_singleton = entity.Clinic()
    start_application(clinic_singleton)
