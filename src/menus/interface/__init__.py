from typing import Callable, Protocol

import tui
from tui.warning import WarningScreen


class Model(Protocol):
    pass


class MainMenu:
    def __init__(
        self, controller: Model, options: list[tuple[Callable, str]]
    ) -> None:
        self.controller = controller
        self._options: list[tuple[Callable, str]] = options

        self._descriptions = options = [desc for func, desc in self._options]
        self._descriptions.append("Sair.")

    def add_option(self, option: Callable, description: str):
        self._options.append((option, description))

    def run(self):
        QUIT_OPTION = len(self._options) + 1
        user_choice = 0

        while True:
            try:
                user_choice = tui.choice(self._descriptions)
            except (ValueError, IndexError) as e:
                WarningScreen(e).render()
                user_choice = -1

            if user_choice == -1:
                continue

            if user_choice == QUIT_OPTION:
                break

            func, desc = self._options[user_choice - 1]
            func(self.controller)

            # try:
            #     func(self.controller)
            # except:
            #     WarningScreen("Função não implementada").render()
