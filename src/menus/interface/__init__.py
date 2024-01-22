from typing import Callable, Protocol

import tui


class Model(Protocol):
    pass


class MainMenu:
    def __init__(self, model: Model, options: list[tuple[str, Callable]]) -> None:
        self.model = model
        self._options: list[tuple[str, Callable]] = options

        self._descriptions = options = [desc for desc, func in self._options]
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
                tui.warn(e)
                user_choice = -1

            if user_choice == -1:
                continue

            if user_choice == QUIT_OPTION:
                break

            desc, func = self._options[user_choice - 1]
            func(self.model)

            # try:
            #     func(self.model)
            # except:
            #     tui.warn("Função não implementada")
