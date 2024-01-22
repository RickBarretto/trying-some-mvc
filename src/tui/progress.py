
from typing import Callable
from ._screen import Screen

def progress(question: list[str] | str, function: Callable, *args, **kwargs):

    def answer() -> bool:
        return "S" == input(">>> ").strip().upper()

    if type(question) is str:
        question = [question]

    question += ["", "Responda [S], caso sim.", "Do contrário, responda qualquer coisa."]

    screen = Screen()
    screen.render_full_screen(question, center=True)

    
    if answer():
        while function(*args, **kwargs):
            pass