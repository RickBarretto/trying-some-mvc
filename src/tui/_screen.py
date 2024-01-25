import os

from tui._utils import (
    clear_screen,
    render_content,
    render_rule,
    render_vertical_space,
    render_default_content
)


class Screen:
    """Um NameSpace que agrupa várias funções de ``_utils.py``."""

    @property
    def width(self) -> int:
        """Retorna a largura do terminal"""
        return os.get_terminal_size().columns

    @property
    def height(self) -> int:
        """Retorna a altura do terminal"""
        return os.get_terminal_size().lines

    def vertical_align(self, content_height: int) -> int:
        """Basicamente é o espaço necessário para alinhar o texto dado um conteúdo"""
        # Remove-se as alturas das bordas e conteúdo, e divide por 2,
        # já que deverá ser impresso antes e após o conteúdo.
        #
        # ``>> 1`` é apenas uma micro-optimização equivalente a ``// 2``.
        return ((self.height - 2) - content_height) >> 1

    def clear_screen(self):
        """Limpa a tela"""
        clear_screen()

    def render_rule(self, width: int | None = None, position: int = 0):
        """Renderiza uma linha horizontal

        Arguments
        ---------
        width: int | None = None
            O tamanho total da largura.
            Se nada for passado, será usado a
            largura atual do terminal do usuário.

        position: int = 0
            Define qual será o contorno usado nos vértices.
            0: Voltado para baixo. (régua do topo)
            1: Voltado para o centro. (régua central)
            2: Voltado para cima. (régua de baixo)

        Assertions
        ----------
        ``position`` deve estar entre 0 e 2.
        """
        assert 0 <= position <= 2
        if width is None:
            width = self.width

        render_rule(width, position)

    def render_content(self, content: list[str], center: bool = False):
        """Renderiza o conteúdo em si.

        Arguments
        ---------
        content: list[str]
            O conteúdo a ser impresso
        center: bool = False
            Se será renderizado horizontalmente ao centro.
        """
        render_content(content, self.width, center)

    def render_vertical_space(
        self, content_height: int | None = None, fixed_height: int | None = None
    ):
        """Renderiza um espaço vertical.

        Arguments
        ---------
        content_height: int | None = None
            Refere-se à altura total do conteúdo,
            o que implica que o espaço renderizado será o equivalente
            ao necessário para centralizá-lo verticalmente na tela.

        fixed_height: int | None = None
            Refere-se à quantidade fixa de linhas em branco
            que serão impressas.

        Notes
        -----
        Em certos casos, convém chamar essa função duas vezes.
        Uma antes e outra após a renderização do conteúdo.

        Assertions
        ----------
        ``content_height`` e ``height`` devem ser passados como argumentos,
        mas nunca ambos ao mesmo tempo.

        """
        assert content_height or fixed_height
        assert not (content_height and fixed_height)

        spaces = (
            fixed_height
            if fixed_height is not None
            else self.vertical_align(content_height)
        )
        render_vertical_space(self.width, spaces)

    def render_full_screen(
        self, content: list[str], status_bar: str = "", center: bool = False
    ):
        """Renderiza em tela cheia.

        Arguments
        ---------
        content: list[str]
            O conteúdo a ser impresso
        status_bar: str = ""
            Uma barra de status. Por padrão não é renderizada
        center: bool = False
            Se o conteúdo deverá ser centralizado ou não.
        """
        content_height = len(content)
        vertical_space = content_height if not status_bar else content_height - 1

        self.clear_screen()
        self.render_rule(position=0)
        if status_bar:
            status_bar = f"{status_bar}   "
            render_default_content(f"{status_bar:>{self.width - 2}}")
        self.render_vertical_space(content_height=vertical_space)
        self.render_content(content, center)
        self.render_vertical_space(content_height=content_height)
        self.render_rule(position=2)

    def wait(self):
        """Espera por uma resposta do usuário.

        Impede que a tela seja atualizada logo em seguida, após chamada.
        """
        _ = input(">>> ")
