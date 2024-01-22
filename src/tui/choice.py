
from ._screen import Screen


def choice(options: list[str]) -> int:
    """Renderiza tela de escolha do usuário e retorna a escolha.

    Example
    -------
    >>> choice(["Opção 1", "Opção 2", "Opção 3", "Opção 4"])
    +-------------------------------------------------------+
    |                                                       |
    |    1 - Opção 1                                        |
    |    2 - Opção 2                                        |
    |    3 - Opção 3                                        |
    |    4 - Opção 4                                        |
    |                                                       |
    |                                                       |
    +-------------------------------------------------------+
    """

    # Declaração de funções internas

    def prefix_option(index: int, content: str) -> str:
        """Prefixa cada linha do conteúdo com uma numeração."""
        TEMPLATE = "{index:<2} - {content}"

        return TEMPLATE.format(
            index=index + 1,
            content=content,
        )

    def format_data(options: list[str]) -> list[str]:
        """Adiciona prefixos para cada linha"""
        return [prefix_option(i, opt) for i, opt in enumerate(options)]

    def user_choice(stop_index: int) -> int:
        """Escolhe uma opção.

        Raises
        ------
        ``ValueError`` caso o valor não possa ser convertido
        ``IndexError`` caso o valor escolhido esteja fora dos índices do menu.
        """
        start_index = 1

        try:
            choosen = int(input(">>> "))
        except:
            raise ValueError("O valor escolhido deve ser um inteiro.") from ValueError

        if start_index <= choosen <= stop_index:
            return choosen
        else:
            raise IndexError(
                f"O valor escolhido deve estar entre {start_index} e {stop_index}."
            )

    # Início da função principal
    screen = Screen()

    # Formata os dados
    data = format_data(options)

    # Imprime os dados
    screen.render_full_screen(data)

    # Retorna a escolha do usuário
    return user_choice(len(options))
