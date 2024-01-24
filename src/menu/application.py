"""Define os menus de início e principal da aplicação"""

import entity
import menu
import tui

from .use_cases import current_session_manager

__all__ = ["start_application"]

# ============= Menu Inicial =============


def start_application(clinic: entity.Clinic):
    """Menu inicial da aplicação.

    Esse menu é apresentado uma única vez ao usuário,
    que irá registrar uma primeira sessão e loggar na mesma,
    e então ser encaminhado para o ``main_menu``.

    Arguments
    ---------
    clinic: Clinic
        Recebe uma instância de ``Clinic``.
        Lembrando que esta deve ser um singleton, e,
        portanto ter uma, e apenas uma única instância da mesma.
    """
    # Apresentação
    tui.splash(
        [
            "Bem-vindo ao Dente Clean Manager!",
            "",
            "Pressione [Enter] para iniciar uma sessão",
        ]
    )

    # Atualiza a sessão
    current_session_manager.update(clinic, first_time=True)

    # Redirecionamento
    main_menu(clinic)


# ============= Menu Principal =============


def main_menu(clinic: entity.Clinic):
    """Menu principal do usuário.

    Onde o usuário poderá gerir a sessão atual (Finalizar ou Atualizar),
    e ter acesso aos menus de recepção e dentista.
    """

    options = [
        ("Iniciar como recepção", menu.reception.start),
        ("Iniciar como dentista", menu.dentist.start),
        ("Atualizar sessão atual", current_session_manager.update),
        ("Finalizar sessão atual", current_session_manager.finish),
    ]

    menu.menu_loop(clinic, options)
