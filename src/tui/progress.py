from ._screen import Screen


def progress(question: list[str] | str) -> bool:
    def answer() -> bool:
        return "S" == input(">>> ").strip().upper()

    if isinstance(question, str):
        question = [question]

    question += [
        "",
        "Responda [S], caso sim.",
        "Do contrário, responda qualquer coisa.",
    ]

    screen = Screen()
    screen.render_full_screen(question, center=True)

    return answer()
