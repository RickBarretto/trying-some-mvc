import os

import tui
from ._screen import Screen


def _fix_options(index: int, line: str):
    return "{tabs}{index:<2} - {content}".format(
        tabs=" " * int(os.get_terminal_size().columns * 0.2),
        index=index + 1,
        content=line,
    )


class ChoiceScreen(Screen):
    def __init__(self, options: list[str]) -> None:
        self._options = options

        # Post init
        self.start = 1
        self.stop = len(options)

    def render(self) -> int:
        """Imprime a tela de escolha de usuário.

        Retorna a quantidade de opções
        """
        options = [_fix_options(i, opt) for i, opt in enumerate(self._options)]

        self.render_full_screen(options)

    def get_value(self) -> int:
        """captura o valor escolhido pelo usuário

        Raises
        ------
            ``ValueError`` em caso de entrada inválida para a conversão de inteiro.
            ``IndexError`` para uma escolha fora da amplitude apresentada ao usuário.
        """
        if self.start <= (inp := int(input(">>> "))) <= self.stop:
            return inp

        raise IndexError()

    def warn_wrong_value(self):
        tui.WarningScreen(
            [
                "Entrada inválida!",
                "",
                f"Sua entrada deve estar entre {self.start} e {self.stop}, sendo um inteiro.",
                "",
            ]
        ).render()
