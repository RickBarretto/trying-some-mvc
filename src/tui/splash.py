from tui._screen import Screen


def splash(content: list[str] | str):
    """Renderiza uma tela com mensagens centralizadas.

    Arguments
    ---------
    content: list[str] | str
        O conteúdo a ser impresso.
        É automaticamente convertido para `list[str]`

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
    content: list[str] = [content] if content is str else content

    screen = Screen()
    screen.render_full_screen(content, center=True)
    screen.wait()
