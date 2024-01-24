from tui._screen import Screen
from tui._utils import left_align_width

__all__ = ["bullet_list"]


def bullet_list(title: str, items: list[str], additional_margin: int = 0):
    """Renderiza uma lista de ``items`` do tipo bullet point.

    Arguments
    ---------
    title: str
        O título da tela
    items: list[str]
        Os elementos a serem impressos
    additional_maring: int = 0
        Margem adicional, caso necessário. 
        Útil quando há quebra de linhas.

    Example
    -------
    >>> bullet_list("ABCD", ["A", "B", "C", "D"])
    +-------------------------------------------------------+
    |                                                       |
    |                       ABCD                            |
    |    - A                                                |
    |    - B                                                |
    |    - C                                                |
    |    - D                                                |
    |                                                       |
    +-------------------------------------------------------+
    """
    screen = Screen()

    title = [title, ""]
    bullet = "◎"  # unicode: 25CE

    lateral_margin = left_align_width() * 2
    max_width = screen.width - lateral_margin

    items = add_bullets(
        items, bullet, max_length=max_width, additional_margin=additional_margin
    )

    screen.clear_screen()
    screen.render_rule(position=0)
    screen.render_vertical_space(fixed_height=2)
    screen.render_content(title, center=True)
    screen.render_content(items)
    screen.render_vertical_space(fixed_height=2)
    screen.render_rule(position=2)
    screen.wait()


def add_bullets(
    content: list[str],
    bullet: str = "*",
    max_length: int = 20,
    additional_margin: int = 0,
) -> list[str]:
    """Adiciona os bullet points no conteúdo.
    
    Arguments
    ---------
    content: list[str]
        Os items a serem impressos
    bullet: str = "*"
        O símbolo a ser usado como bullet point
    max_length: int = 20
        O tamanho máximo que uma string pode possuir
    additional_margin: int = 0
        Margem adicional caso necessário.
        Útil para alinhar a quebra de linha.
    """
    result = []

    bullet_prefix = f" {bullet}  "
    align_prefix = " " * (len(bullet_prefix) + additional_margin)

    for item in content:
        lines: list[str] = break_line(item, max_length, additional_margin)
        lines[0] = bullet_prefix + lines[0]
        for i in range(1, len(lines)):
            lines[i] = align_prefix + lines[i]

        result += lines

    return result


def break_line(content: str, max_length: int = 20, additional_margin: int = 0) -> list[str]:
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

    for i, el in enumerate(content):
        is_whitespace = el == " "
        reached_line_limit = (i - line_start) >= max_length

        if len(result) == 1:
            max_length -= additional_margin

        if is_whitespace:
            last_whitespace = i

        if is_whitespace and reached_line_limit:
            result.append(content[line_start:last_whitespace])
            line_start = i + 1

    result.append(content[line_start:])

    return result
