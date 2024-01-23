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


def render_rule(inner_width: int, position: int = 0):
    """
    Arguments
    ---------
    position: int = 0
        0: para topo
        1: para meio
        2: para baixo
    """
    dash = "─"  # unicode: 2500
    corners = {
        0: ("╭", "╮"),  # unicode: (256D, 256E)
        1: ("├", "┤"),  # unicode: (251C, 2524)
        2: ("╰", "╯"),  # unicode: (2570, 256F)
    }
    print(corners[position][0], (dash * inner_width), corners[position][1], sep="")


def render_default_content(content: str):
    vertical_bar = "│"  # unicode: 2502
    print(vertical_bar, content, vertical_bar, sep="")


def render_content(content: str, inner_width: int, center: bool = False):
    # define o posicionamento de ``content`` de acordo com ``center``
    pos = "^" if center else "<"
    tab = left_align_width() if not center else 0

    for line in content:
        # Imprime "|        <conteúdo>      |" para ``center = True``
        # Imprime "|<conteúdo>              |" para ``center = False``
        line = line.strip()
        prefix = " " * tab
        render_default_content(f"{prefix}{line:{pos}{inner_width - tab}}")

def left_align_width():
    return int(os.get_terminal_size().columns * 0.2)


def render_vertical_space(inner_width: int, height: int):
    for _ in range(height - 1):
        # Imprime "|        <espaço em branco>      |"
        render_default_content(" " * inner_width)
