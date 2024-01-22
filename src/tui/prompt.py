from ._screen import Screen

def prompt(ask: str, suggestion: str = "") -> str:
    """
    
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
    |      >>>|                                             |
    """

    content = [ask]
    content.append(suggestion)

    screen = Screen()

    visual_contents_height = 3 # 3 = (2 horizonntal rules + 1 input line)
    content_height = (screen.height - len(content) - visual_contents_height) >> 1 # >> 1 == // 2

    screen.clear_screen()
    screen.render_rule(position=0)
    screen.render_vertical_space(height=content_height)
    screen.render_content(content, center=True)
    screen.render_vertical_space(height=content_height)
    screen.render_rule(position=2)
    return input(" >>> ").strip()








def multiline(message: str) -> list[str]:
    print(message)
    print("(Linha vazia para finalizar.)")

    result = []
    while inp := input(">>> ").strip():
        result.append(inp)

    return result
