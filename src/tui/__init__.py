"""Todas as telas disponíveis para uso.

As telas serão usadas pelas classes de ``src.singleton``.
"""

from .main_menu import MainMenu
from .choice import ChoiceScreen
from .list import ListScreen
from .prompt import Prompt
from .splash import SplashScreen
from .warning import WarningScreen

__all__ = [
    "MainMenu",
    "ChoiceScreen",
    "ListScreen",
    "Prompt",
    "SplashScreen",
    "WarningScreen",
]
