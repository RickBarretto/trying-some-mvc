"""Módulo principal
"""

import entity
from app import start


if __name__ == "__main__":
    clinic = entity.Clinic()
    start(clinic)
