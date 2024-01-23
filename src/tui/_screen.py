import os

from tui._utils import (
    clear_screen,
    render_content,
    render_rule,
    render_vertical_space,
    render_default_content
)


class Screen:
    @property
    def width(self):
        return os.get_terminal_size().columns

    @property
    def height(self):
        return os.get_terminal_size().lines

    @property
    def inner_width(self):
        return self.width - 2

    @property
    def inner_height(self):
        return self.height - 2

    def vertical_align(self, content_height: int):
        """Basicamente é o espaço necessário para alinhar o texto"""
        # Remove-se as alturas das bordas e conteúdo, e divide por 2,
        # já que deverá ser impresso antes e após o conteúdo.
        #
        # ``>> 1`` é apenas uma micro-optimização equivalente a ``// 2``.
        return (self.inner_height - content_height) >> 1

    def clear_screen(self):
        clear_screen()

    def render_rule(self, width: int | None = None, position: int = 0):
        width = width - 2 if width is not None else self.inner_width
        render_rule(width, position)

    def render_content(self, content: list[str], center: bool = False):
        render_content(content, self.inner_width, center)

    def render_vertical_space(
        self, content_height: int | None = None, height: int | None = None
    ):
        assert content_height or height
        assert not (content_height and height)

        spaces = height if height is not None else self.vertical_align(content_height)
        render_vertical_space(self.inner_width, spaces)

    def render_full_screen(self, content: list[str], status_bar: str = "", center=False):
        content_height = len(content)

        vertical_space = content_height if not status_bar else content_height - 1

        self.clear_screen()

        self.render_rule(position=0)
        if status_bar:
            status_bar = f"{status_bar}   "
            render_default_content(f"{status_bar:>{self.inner_width}}")
        self.render_vertical_space(content_height=vertical_space)
        self.render_content(content, center)
        self.render_vertical_space(content_height=content_height)
        self.render_rule(position=2)

    def wait(self):
        _ = input(">>> ")
