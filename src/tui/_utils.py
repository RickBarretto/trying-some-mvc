import os


# ============= Funções de alinhamento =============


def terminal_size() -> tuple[int, int]:
    """Retorna o tamanho do terminal em formato de ``tuple[int, int]``"""
    size = os.get_terminal_size()
    return size.columns, size.lines


def left_align_width() -> int:
    """Retorna o espaço necessário para a margem esquerda."""
    return int(os.get_terminal_size().columns * 0.2)


# ============= Funções de impressão de conteúdo =============


def clear_screen():
    """Limpa a tela do usuário.

    Automaticamente reconhece o sistema operacional do usuário.
    """
    match os.name:
        case "nt":
            os.system("cls")
        case _:
            os.system("clear")


def render_rule(width: int, position: int = 0):
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
    print(corners[position][0], (dash * (width - 2)), corners[position][1], sep="")


def render_default_content(content: str):
    """Renderiza o conteúdo, sem alinhamento."""
    vertical_bar = "│"  # unicode: 2502
    print(vertical_bar, content, vertical_bar, sep="")


def render_content(content: list[str], width: int, center: bool = False):
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
        render_default_content(f"{prefix}{line:{pos}{width - 2 - tab}}")


def render_vertical_space(width: int, height: int):
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
        render_default_content(" " * (width - 2))


# ============= Funções de manipulação de dados =============


def normalize_lines(content: list[str], max_length: int) -> list[str]:
    """Quebra as linhas do conteúdo para encaixar em ``max_length``."""
    result = []

    for item in content:
        lines: list[str] = break_line(item, max_length)
        result += lines

    return result


def break_line(
    content: str, max_length: int = 20, additional_margin: int = 0
) -> list[str]:
    """Algoritmo que quebra a linha por espaços em branco.

    Arguments
    ---------
    content: str
        O item
    max_length: int = 20
        O tamanho máximo que a string pode possuir
    additional_margin: int = 0
        Margem adicional da linha.
    """
    result = []

    line_start = 0
    last_whitespace = 0
    secondary_lines_max = max_length - additional_margin

    for i, el in enumerate(content):
        is_whitespace = el == " "
        reached_line_limit = (i - line_start) >= max_length

        if is_whitespace:
            last_whitespace = i

        if is_whitespace and reached_line_limit:
            result.append(content[line_start:last_whitespace])
            line_start = i + 1
            max_length = secondary_lines_max

    result.append(content[line_start:])

    return result
