from tui._utils import render_rule, render_content, render_vertical_space
from tui._screen import Screen


class ListScreen(Screen):
    def __init__(self, title: str, items: list) -> None:
        self.title = title
        self.items = items

    def render(self):
        title = [self.title.upper(), ""]
        items = [f" - {item}" for item in self.items]

        self.clear_screen()
        self.render_rule()
        self.render_vertical_space(height=2)
        self.render_content(title, center=True)
        self.render_content(items)
        self.render_vertical_space(height=2)
        self.render_rule()
        self.wait()
