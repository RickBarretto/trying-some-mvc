from tui._screen import Screen


class SplashScreen(Screen):
    """Renderiza uma tela com mensagens centralizadas.

    Arguments
    ---------
    content: list[str] | str
        O conteúdo a ser impresso.
        É automaticamente convertido para `list[str]`

    """

    def __init__(self, content: list[str] | str) -> None:
        self.content: list[str] = [content] if content is str else content

    def render(self):
        """Renderiza e espera pelo input do usuário.

        Example
        -------
        >>> SplashScreen("Bem vindo!").render()
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
        content = self.content
        self.render_full_screen(content, center=True)
        self.wait()
