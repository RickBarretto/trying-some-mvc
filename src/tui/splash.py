from tui._screen import Screen


def splash(content: list[str] | str):
    """Renderiza uma tela com mensagens centralizadas.

    Example
    -------
    >>> splash("Bem vindo!")
    +-------------------------------------------------------+
    |                                                       |
    |                                                       |
    |                                                       |
    |                     Bem vindo!                        |
    |                                                       |
    |                                                       |
    |                                                       |
    +-------------------------------------------------------+
    """
    if isinstance(content, str):
        content = [content]

    screen = Screen()
    screen.render_full_screen(content, center=True)
    screen.wait()
