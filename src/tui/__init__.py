"""Todas as telas disponíveis para uso.

As telas serão usadas pelas classes de ``src.menus``.
"""

from .choice import choice
from .hint import info, warn
from .list import bullet_list
from .proceed import proceed
from .prompt import prompt, multiline
from .splash import splash

__all__ = [
    "choice",
    "bullet_list",
    "info",
    "multiline",
    "proceed",
    "prompt",
    "splash",
    "warn",
]
