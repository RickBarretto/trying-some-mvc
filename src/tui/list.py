from tui._screen import Screen
from tui._utils import left_align_width

__all__ = ["bullet_list"]

def bullet_list(title: str, items: list):
    """Renderiza uma lista de ``items`` do tipo bullet point.

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
    
    title = [title.upper(), ""]
    bullet = "◎"  # unicode: 25CE

    lateral_margin = (left_align_width() * 2)
    max_width = screen.width - lateral_margin 

    items = add_bullets(items, bullet, max_length=max_width)

    screen.clear_screen()
    screen.render_rule(position=0)
    screen.render_vertical_space(height=2)
    screen.render_content(title, center=True)
    screen.render_content(items)
    screen.render_vertical_space(height=2)
    screen.render_rule(position=2)
    screen.wait()


def add_bullets(content: list[list[str]], bullet = "*", max_length = 20) -> list[str]:
    result = []

    bullet_prefix = f" {bullet}  "
    align_prefix = " " * len(bullet_prefix)

    for item in content:
        lines: list[str] = break_line(item, max_length)
        lines[0] = bullet_prefix + lines[0]
        for i in range(1, len(lines)):
            lines[i] = align_prefix + lines[i]

        result += lines

    return result


def break_line(content: str, max_length = 20) -> list[str]:
    result = []

    line_start = 0
    last_whitespace = 0

    for i, el in enumerate(content):
        is_whitespace = el == " "
        reached_line_limit = (i - line_start) >= max_length
        
        if is_whitespace:
            last_whitespace = i

        if is_whitespace and reached_line_limit:
            result.append(content[line_start:last_whitespace])
            line_start = i + 1
        
    result.append(content[line_start:])

    return result