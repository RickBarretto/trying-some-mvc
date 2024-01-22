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

    # Adiciona símbolo de aviso ao início
    content[0] = "🛈 - " + content[0] # unicode: 1F6C8

    # Adiciona mensagem para continuar ao fim
    content.append("")
    content.append("Pressione [Enter] para continuar.")

    # Renderiza a tela e espera por entrada.
    screen.render_full_screen(content, center=True)
    screen.wait()
