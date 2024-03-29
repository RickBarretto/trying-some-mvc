from ._screen import Screen


def prompt(ask: str, suggestion: str = "") -> str:
    """Imprime uma pergunta ao usuário. Podendo ser passada uma sugestão.

    Example
    -------
    >>> prompt("Insira o CPF do paciente.", "Formato: XXX.XXX.XXX-XX")
    +-------------------------------------------------------+
    |                                                       |
    |              Insira o CPF do paciente                 |
    |                                                       |
    |              Formato: XXX.XXX.XXX-XX                  |
    |                                                       |
    +-------------------------------------------------------+
           >>>|
    """

    content = [ask]
    content.append("")
    content.append(suggestion)

    screen = Screen()

    visual_contents_height = 3  # 3 = (2 horizonntal rules + 1 input line)
    content_height = (
        screen.height - len(content) - visual_contents_height
    ) >> 1  # >> 1 é uma micro optimização para // 2

    screen.clear_screen()
    screen.render_rule(position=0)
    screen.render_vertical_space(fixed_height=content_height)
    screen.render_content(content, center=True)
    screen.render_vertical_space(fixed_height=content_height)
    screen.render_rule(position=2)
    return input(" >>> ").strip()


def multiline(message: str) -> list[str]:
    """Pede input do usuário em múltiplas linhas.

    Example
    -------
    >>> multiline("Insira informações extra paciente.")
    +-------------------------------------------------------+
    |        Insira informações extra do paciente           |
    |            [linha vazia para finalizar]               |
    +-------------------------------------------------------+
    /   >>>|                                                /
    /                                                       /
    /                                                       /
    /                                                       /
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/

    """
    content = [message]
    content.append("")
    content.append("[Linha vazia para finalizar]")

    screen = Screen()

    screen.clear_screen()
    screen.render_rule()
    screen.render_vertical_space(fixed_height=3)
    screen.render_content(content, center=True)
    screen.render_vertical_space(fixed_height=3)
    screen.render_rule(position=2)

    result = []
    while inp := input(">>> ").strip():
        result.append(inp)

    return result
