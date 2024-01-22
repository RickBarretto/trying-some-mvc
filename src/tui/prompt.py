from ._screen import Screen

def prompt(ask: str, suggestion: str = "") -> str:
    """
    
    Example
    -------
    >>> prompt("Insira o CPF do paciente.", "Formato: XXX.XXX.XXX-XX")
    +-------------------------------------------------------+
    |                                                       |
    |              Insira o CPF do paciente                 |
    |                                                       |
    |              Formato: XXX.XXX.XXX-XX                  |
    |                                                       |
    +-------------------------------------------------------+
    |      >>>|                                             |
    """

    content = [ask]
    content.append(suggestion)

    screen = Screen()

    visual_contents_height = 3 # 3 = (2 horizonntal rules + 1 input line)
    content_height = (screen.height - len(content) - visual_contents_height) >> 1 # >> 1 == // 2

    screen.clear_screen()
    screen.render_rule(position=0)
    screen.render_vertical_space(height=content_height)
    screen.render_content(content, center=True)
    screen.render_vertical_space(height=content_height)
    screen.render_rule(position=2)
    return input(" >>> ")


def get_date(custom_message: str = "Insira uma data.") -> str:
    date = prompt(custom_message)
    date_slots = date.split("/")

    ERROR_MESSAGE = ("Formato de data inválido.", "Formato correto: DD/MM/YYYY")

    if len(date_slots) != 3:
        raise ValueError(*ERROR_MESSAGE)

    for i, length in enumerate([2, 2, 4]):
        if len(date_slots[i]) != length:
            raise ValueError(*ERROR_MESSAGE)

    return date


def get_cpf(custom_message: str = "Insira o CPF.") -> str:
    INVALID_CPF_MSG = "Formato de CPF inválido!"
    FORMAT_SUGGESTION_MSG = "A formatação deve ser 'DDD.DDD.DDD-DD'"

    cpf = prompt(custom_message)

    if len(cpf) != 14:
        raise ValueError(
            INVALID_CPF_MSG,
            "Verifique se a quantidade de dígitos está correta.",
            FORMAT_SUGGESTION_MSG,
        )

    for sep, idx in [(".", 3), (".", 7), ("-", 11)]:
        if cpf[idx] != sep:
            raise ValueError(
                INVALID_CPF_MSG,
                "Os separadores estão errados",
                FORMAT_SUGGESTION_MSG,
            )

    cpf_digits: str = cpf.replace("-", "").replace(".", "")

    if not cpf_digits.isdigit():
        raise ValueError(
            INVALID_CPF_MSG,
            "Verifique a presença de letras ou outros símbolos.",
            FORMAT_SUGGESTION_MSG,
        )

    if len(cpf_digits) != 11:
        raise ValueError(
            INVALID_CPF_MSG,
            "Verifique se a quantidade de dígitos está correta.",
            FORMAT_SUGGESTION_MSG,
        )

    return cpf


def multiline(message: str) -> list[str]:
    print(message)
    print("(Linha vazia para finalizar.)")

    result = []
    while inp := input(">>> ").strip():
        result.append(inp)

    return result
