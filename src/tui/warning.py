from tui._screen import Screen


class WarningScreen(Screen):
    """Define uma tela de avisos

    Args
    ----
    content: str | list[str] | Exception
        Recebe ``content`` para imprimí-lo na tela.
        Esse argumento é automaticamente convertido para o tipo ``list[str]``.
    """

    def __init__(self, content: str | list[str] | Exception) -> None:
        # Converte ``content`` para o tipo correto
        match content:
            case str():  # põe ``content`` dentro de uma lista
                content = [content]
            case Exception():  # converte ``Exception.args`` para lista
                content = list(content.args)  # note que args é do tipo ``tuple``
            case _:
                pass

        # Atribuindo variável
        self.content = content

    def render(self):
        """Imprime um aviso ao usuário.

        Será posto um símbolo de aviso ao início e uma mensagem de proseguir ao fim.

        Example
        -------
        >>> WarningScreen("Paciente não pode ser registrado!").render()
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

        content = self.content

        # Adiciona símbolo de aviso ao início
        content[0] = "[!] - " + content[0]

        # Adiciona mensagem para continuar ao fim
        content.append("")
        content.append("Pressione [Enter] para continuar.")

        # Renderiza a tela e espera por entrada.
        self.render_full_screen(content, center=True)
        self.wait()
