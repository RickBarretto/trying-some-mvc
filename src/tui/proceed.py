from ._screen import Screen
from ._utils import normalize_lines


def proceed(question: list[str] | str) -> bool:
    """
    Example
    -------
    >>> proceed("Desejas registrar?")
    +-------------------------------------------------------+
    |                                                       |
    |                                                       |
    |                 Desejas registrar?                    |
    |                                                       |
    |                  [Enter] |  [Sim]                     |
    |                                                       |
    |                                                       |
    +-------------------------------------------------------+
    """

    def answer() -> bool:
        return "S" == input(">>> ").strip().upper()

    if isinstance(question, str):
        question = [question]

    screen = Screen()

    cancel_message = "[Enter] Cancelar"
    confirm_message = "[S] Sim"

    question += [
        "",
        f"{confirm_message} | {cancel_message}",
    ]

    question = normalize_lines(question, screen.width - 4)
    screen.render_full_screen(question, center=True)

    return answer()
