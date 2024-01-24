from ._screen import Screen


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

    cancel_message = "[Enter] Cancelar"
    confirm_message = "[S] Sim"
    max_side_size = max(len(cancel_message), len(confirm_message))
    

    question += ["", f"{confirm_message:<{max_side_size}} | {cancel_message:>{max_side_size}}"]

    screen = Screen()
    screen.render_full_screen(question, center=True)

    return answer()
