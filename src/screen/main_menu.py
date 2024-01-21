from typing import Callable, Protocol

from screen.choice import ChoiceScreen
from screen.warning import WarningScreen


class Controller(Protocol):
    pass


class MainMenu:
    def __init__(
        self, controller: Controller, options: list[tuple[Callable, str]]
    ) -> None:
        self.controller = controller
        self._options: list[tuple[Callable, str]] = options

        self._descriptions = options = [desc for func, desc in self._options]
        self._descriptions.append("Sair.")

    def add_option(self, option: Callable, description: str):
        self._options.append((option, description))

    def show_menu(self):
        self.screen = ChoiceScreen(self._descriptions)
        self.screen.render()

    def get_input(self) -> int:
        try:
            return self.screen.get_value()
        except:
            self.screen.warn_wrong_value()
            return -1

    def run(self):
        QUIT_OPTION = len(self._options) + 1
        choice = 0

        while True:
            self.show_menu()
            choice: int = self.get_input()

            if choice == -1:
                continue

            if choice == QUIT_OPTION:
                break

            func, desc = self._options[choice - 1]
            func(self.controller)

            # try:
            #     func(self.controller)
            # except:
            #     WarningScreen("Função não implementada").render()
