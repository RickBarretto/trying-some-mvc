import os


def clear_screen():
    """Limpa a tela do usuário.

    Automaticamente reconhece o sistema operacional do usuário.
    """
    match os.name:
        case "nt":
            os.system("cls")
        case _:
            os.system("clear")


def terminal_size() -> tuple[int, int]:
    """Retorna o tamanho do terminal em formato de ``tuple[int, int]``"""
    size = os.get_terminal_size()
    return size.columns, size.lines


def render_rule(inner_width: int, bottom: bool = False):
    # Imprime "+------------------------+"
    print("+", ("-" * inner_width), "+", sep="")


def render_content(content: str, inner_width: int, center: bool = False):
    # define o posicionamento de ``content`` de acordo com ``center``
    pos = "^" if center else "<"

    for line in content:
        # Imprime "|        <conteúdo>      |" para ``center = True``
        # Imprime "|<conteúdo>              |" para ``center = False``
        print("|", f"{line:{pos}{inner_width}}", "|", sep="")


def render_vertical_space(inner_width: int, height: int):
    for _ in range(height - 1):
        # Imprime "|        <espaço em branco>      |"
        print("|", (" " * inner_width), "|", sep="")
