from tui._screen import Screen


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
    title = [title.upper(), ""]
    items = [f" ◎ {item}" for item in items]

    screen = Screen()
    screen.clear_screen()
    screen.render_rule(position=0)
    screen.render_vertical_space(height=2)
    screen.render_content(title, center=True)
    screen.render_content(items)
    screen.render_vertical_space(height=2)
    screen.render_rule(position=2)
    screen.wait()
