"""Define os casos de uso de prompts comuns que pedem e validam entradas do usuário"""

from typing import Callable
import tui


__all__ = ["patient_cpf", "session_date"]

# ============= Prompts =============


def patient_cpf() -> str:
    """Pede ao usuário o CPF do paciente até que este seja válido."""
    question = "Insira o CPF do paciente:"
    cpf_format = "XXX.XXX.XXX-XX"
    suggestion = f"Formato: {cpf_format}"
    warning = "CPF inválido!"

    return _request(question, suggestion, warning, cpf_format, _is_valid_cpf)


def session_date() -> str:
    """Pede ao usuário uma data até que esta seja válida."""
    question = "Insira uma data:"
    date_format = "DD/MM/YYYY"
    suggestion = f"Formato: {date_format}"
    warning = "Formato de data inválido!"

    return _request(question, suggestion, warning, date_format, _is_valid_date)


# ============= Validadores de entradas =============


def _is_valid_cpf(entry: str) -> bool:
    """Valida se uma entrada é um CPF válido."""
    fields = entry.replace("-", ".").split(".")

    # Verifica os separadores

    # Os respectivos separadores devem estar em
    # XXX.XXX.XXX-XX
    #    ^   ^   ^
    #    3   7   11

    has_dot_at_index_3_and_7 = [3, 7] == [
        index for index, char in enumerate(entry) if char == "."
    ]
    has_dash_at_index_11 = [11] == [
        index for index, char in enumerate(entry) if char == "-"
    ]

    # Verifica os campos de preenchimento
    try:
        has_4_fields = 4 == len(fields)
        all_fields_are_digits = all((field.isdigit() for field in fields))
        first_3_fields_has_3_digits = all((3 == len(field) for field in fields[0:3]))
        last_field_has_2_digits = 2 == len(fields[-1])
    except IndexError:
        return False

    return all(
        (
            has_dot_at_index_3_and_7,
            has_dash_at_index_11,
            has_4_fields,
            all_fields_are_digits,
            first_3_fields_has_3_digits,
            last_field_has_2_digits,
        )
    )


def _is_valid_date(entry: str) -> bool:
    """Valida se uma entrada é uma data válida."""
    fields = entry.split("/")

    # Verifica os campos de preenchimento
    has_three_fields = 3 == len(fields)
    all_fields_are_digits = all((field.isdigit() for field in fields))

    # Verifica cada campo individualmente

    # O formato deve seguir o formato brasileiro:
    #   DD/MM/YYYY

    try:
        day_has_two_digits = 2 == len(fields[0])
        month_has_two_digits = 2 == len(fields[1])
        year_has_four_digits = 4 == len(fields[2])
    except IndexError:
        return False

    return all(
        (
            has_three_fields,
            all_fields_are_digits,
            day_has_two_digits,
            month_has_two_digits,
            year_has_four_digits,
        )
    )


# ============= Função interna =============


def _request(
    question: str,
    suggestion: str,
    warning: str,
    data_format: str,
    validator: Callable[[str], bool],
) -> str:
    """Função abstrata usada para fazer a requisição ao usuário.

    Arguments
    ---------
    question: str
        A pergunta ou requisição.
    suggestion: str
        Sugestão relacionada à entrada.
    warning: str
        O aviso, caso o usuáiro insira dados inválidos.
    format: str
        Um template ou exemplo de entrada válida.
    validator: Callable[[str], bool]
        Uma função validadora da entrada.
    """
    while not validator(value := tui.prompt(question, suggestion)):
        tui.warn([warning, f"Verifique se o formato condiz com '{data_format}'."])

    return value
