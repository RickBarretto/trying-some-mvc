from ._screen import Screen


def progress(question: list[str] | str) -> bool:
    def answer() -> bool:
        return "S" == input(">>> ").strip().upper()

    if isinstance(question, str):
        question = [question]

    cancel_message = "[Enter] Cancelar"
    confirm_message = "[S] Sim"
    confirm_message = f"{confirm_message:>{len(cancel_message)}}"

    question += [
        "",
         f"{confirm_message} | {cancel_message}"
    ]

    screen = Screen()
    screen.render_full_screen(question, center=True)

    return answer()
