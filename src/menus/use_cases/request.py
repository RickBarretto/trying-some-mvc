from typing import Callable
import tui


__all__ = ["patient_cpf", "session_date"]


def patient_cpf() -> str:
    question = "Insira o CPF do paciente."
    format = "XXX.XXX.XXX-XX"
    suggestion = f"Formato: {format}"
    warning = "CPF inválido"
    
    return _request(question, suggestion, warning, format, _is_valid_cpf)

def session_date() -> str:
    question = "Insira uma data."
    format = "DD/MM/YYYY"
    suggestion = f"Formato: {format}"
    warning = "Formato de data inválido."

    return _request(question, suggestion, warning, format, _is_valid_date)


def _request(question: str, suggestion: str, warning: str, format: str, validator: Callable[[str], bool]) -> str:
    while not validator(value := tui.prompt(question, suggestion)):
        tui.warn([
            warning,
            f"Verifique se o formato condiz com {format}"
        ])

    return value

def _is_valid_cpf(entry: str) -> bool:

    fields = entry.replace("-", ".").split(".")

    # Verifica os separadores

    # Os respectivos separadores devem estar em
    # XXX.XXX.XXX-XX
    #    ^   ^   ^
    #    3   7   11

    has_dot_at_index_3_and_7 = [3, 7] == [index for index, char in enumerate(entry) if char == "."]
    has_dash_at_index_11 = [11] == [index for index, char in enumerate(entry) if char == "-"]
    
    # Verifica os campos de preenchimento
    try:
        has_4_fields                = 4 == len(fields)
        all_fields_are_digits       = all((field.isdigit() for field in fields))
        first_3_fields_has_3_digits = all((3 == len(field) for field in fields[0:3]))
        last_field_has_2_digits     = 2 == len(fields[-1])
    except IndexError:
        return False

    return all((
        has_dot_at_index_3_and_7,
        has_dash_at_index_11,
        has_4_fields,
        all_fields_are_digits,
        first_3_fields_has_3_digits,
        last_field_has_2_digits
    ))

def _is_valid_date(entry: str) -> bool:

    fields = entry.split("/")

    # Verifica os campos de preenchimento
    has_three_fields      = 3 == len(fields)
    all_fields_are_digits = all((field.isdigit() for field in fields))

    # Verifica cada campo individualmente

    # O formato deve seguir o formato brasileiro:
    #   DD/MM/YYYY

    try:
        day_has_two_digits    = 2 == len(fields[0])
        month_has_two_digits  = 2 == len(fields[1])
        year_has_four_digits  = 4 == len(fields[2])
    except IndexError:
        return False

    return all((
        has_three_fields, 
        all_fields_are_digits, 
        day_has_two_digits, 
        month_has_two_digits, 
        year_has_four_digits
    ))