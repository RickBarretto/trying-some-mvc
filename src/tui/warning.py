from tui._screen import Screen


def warn(content: str | list[str] | Exception) -> None:
    """Define uma tela de avisos.

    Será posto um símbolo de aviso ao início e uma mensagem de proseguir ao fim.

    Arguments
    ---------
    content: str | list[str] | Exception
        Recebe ``content`` para imprimí-lo na tela.
        Esse argumento é automaticamente convertido para o tipo ``list[str]``.

    Example
        -------
        >>> warn("Paciente não pode ser registrado!")
        +-------------------------------------------------------+
        |                                                       |
        |                                                       |
        |        [!] - Paciente não pode ser registrado!        |
        |                                                       |
        |           Pressione [Enter] para continuar.           |
        |                                                       |
        |                                                       |
        +-------------------------------------------------------+
    """

    # Defnie funções internas
    def to_list_str(content: str | list[str] | Exception) -> list[str]:
        """Converte ``content`` para o tipo correto"""
        match content:
            case str():  # põe ``content`` dentro de uma lista
                return [content]
            case Exception():  # converte ``Exception.args`` para lista
                return list(content.args)  # note que args é do tipo ``tuple``
            case _:
                return content

    # Inicio da função principal
    screen = Screen()

    # Corrige o tipo de content
    content = to_list_str(content)

    # Adiciona símbolo de aviso ao início
    content[0] = "⚠ " + content[0] # unicode: 26A0

    # Adiciona mensagem para continuar ao fim
    content.append("")
    content.append("Pressione [Enter] para continuar.")

    # Renderiza a tela e espera por entrada.
    screen.render_full_screen(content, center=True)
    screen.wait()
