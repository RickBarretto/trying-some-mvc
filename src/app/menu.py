"""Define um menu genérico base."""

from typing import Callable, Protocol

import entity
import tui

# ============= Definição de protocolos =============


class Model(Protocol):
    """Apenas um placeholder para a tipagem."""


class MenuOption(Protocol):
    """Apenas um placeholder para a tipagem"""

    def __call__(self, clinic: entity.Clinic, *args, **kwargs):
        pass


# ============= Definição de função default =============


def default_status(model: Model) -> str:
    """Retorna uma string vazia.

    Suprimi a impressão do status no menu por padrão.
    """
    return ""


# ============= Definição de função principal =============


def menu_loop(
    model: Model,
    options: list[tuple[str, MenuOption]],
    status_func: Callable[[Model], str] = default_status,
) -> None:
    # Filtro de informações

    use_cases = [use_case for _, use_case in options]  # As ações do menu
    descriptions = [desc for desc, _ in options]  # As descrições de cada ação

    # Adiciona a descrição para a ação virtual 'sair'
    descriptions.append("Sair")

    # Declarações de constantes de escolha

    QUIT_OPTION = len(options) + 1  # Índice da ação virtual de 'sair'
    INVALID_CHOICE = -1  # Caso a escolha seja inválida

    while True:
        # Validação da entrada do usuário
        try:
            user_choice = tui.choice(descriptions, status_func(model))
        except (ValueError, IndexError) as e:
            tui.warn(e)
            user_choice = INVALID_CHOICE

        if user_choice == INVALID_CHOICE:
            continue

        if user_choice == QUIT_OPTION:
            break

        # Chama a ação correspondente à escolha do usuário
        use_cases[user_choice - 1](model)
