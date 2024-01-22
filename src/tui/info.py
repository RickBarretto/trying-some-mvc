from tui._screen import Screen


def info(content: str | list[str]) -> None:
    """Define uma tela de avisos.

    Será posto um símbolo de aviso ao início e uma mensagem de proseguir ao fim.

    Arguments
    ---------
    content: str | list[str]
        Recebe ``content`` para imprimí-lo na tela.
        Esse argumento é automaticamente convertido para o tipo ``list[str]``.

    Example
        -------
        >>> info("Paciente registrado!")
        +-------------------------------------------------------+
        |                                                       |
        |                                                       |
        |              [i] - Paciente registrado!               |
        |                                                       |
        |           Pressione [Enter] para continuar.           |
        |                                                       |
        |                                                       |
        +-------------------------------------------------------+
    """

    if type(content) is str:
        content = [content]

    screen = Screen()
    symbol = "🛈"  # unicode: 1F6C8

    # Adiciona símbolo de aviso ao início
    content[0] = f"{symbol}  {content[0]} {symbol}"

    # Adiciona mensagem para continuar ao fim
    content += ["", "Pressione [Enter] para continuar."]

    # Renderiza a tela e espera por entrada.
    screen.render_full_screen(content, center=True)
    screen.wait()
