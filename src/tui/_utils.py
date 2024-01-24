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
    """Renderiza uma régua horizontal
    
    Arguments
    ---------
    position: int = 0
        0: para topo
        1: para meio
        2: para baixo

    Assertions
    ----------
    ``position`` deve estar entre 0 e 2
    """
    assert 0 <= position <= 2

    dash = "─"  # unicode: 2500
    corners = {
        0: ("╭", "╮"),  # unicode: (256D, 256E)
        1: ("├", "┤"),  # unicode: (251C, 2524)
        2: ("╰", "╯"),  # unicode: (2570, 256F)
    }
    print(corners[position][0], (dash * inner_width), corners[position][1], sep="")


def render_default_content(content: str):
    """Renderiza o conteúdo, sem alinhamento."""
    vertical_bar = "│"  # unicode: 2502
    print(vertical_bar, content, vertical_bar, sep="")


def render_content(content: str, inner_width: int, center: bool = False):
    """Renderiza o conteúdo alinhando-o.

    Arguments
    ---------
    content: str
        O conteúdo em si
    inner_width: int
        Define o espaço interno do conteúdo
    center: bool = False
        Determina se o conteúdo será centralizado ou não.
    """
    # define o posicionamento de ``content`` de acordo com ``center``
    pos = "^" if center else "<"
    tab = left_align_width() if not center else 0

    for line in content:
        # Imprime "|        <conteúdo>      |" para ``center = True``
        # ou
        # Imprime "|<conteúdo>              |" para ``center = False``
        line = line.rstrip()
        prefix = " " * tab
        render_default_content(f"{prefix}{line:{pos}{inner_width - tab}}")


def left_align_width() -> int:
    """Retorna o espaço necessário para a margem esquerda."""
    return int(os.get_terminal_size().columns * 0.2)


def render_vertical_space(inner_width: int, height: int):
    """Renderiza um espaço vertical.

    Arguments
    ---------
    inner_width: int
        O tamanho interno desse espaço
    height: int
        A altura desse espaço
    """
    for _ in range(height - 1):
        # Imprime "|        <espaço em branco>      |"
        render_default_content(" " * inner_width)
