import os

from ._screen import Screen


def choice(options: list[str]) -> int:

    def prefix_option(index: int, content: str) -> str:
        TEMPLATE = "{tabs}{index:<2} - {content}"

        return TEMPLATE.format(
            tabs=" " * int(os.get_terminal_size().columns * 0.2),
            index=index + 1,
            content=content,
        )
    
    def format_data(options: list[str]) -> list[str]:
        return [prefix_option(i, opt) for i, opt in enumerate(options)]
    
    def user_choice(stop_index: int) -> int:
        start_index = 1

        try:
            choosen = int(input(">>> "))
        except:
            raise ValueError("O valor escolhido deve ser um inteiro.") from ValueError

        if start_index <= choosen <= stop_index:
            return choosen
        else:
            raise IndexError(f"O valor escolhido deve estar entre {start_index} e {stop_index}.")

    screen = Screen()

    # Formata os dados
    data = format_data(options)
    
    # Imprime os dados
    screen.render_full_screen(data)

    # Retorna a escolha do usuário
    return user_choice(len(options))
