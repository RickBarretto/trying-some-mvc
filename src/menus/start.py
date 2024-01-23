from entities.clinic import Clinic
from menus.interface import MainMenu
from menus.use_cases import current_session_manager
from menus import dentist, reception
import tui

__all__ = ["start_application"]


def main_menu(clinic: Clinic):

    current_session_manager.update(clinic)

    options = [
            ("Iniciar como recepção.", reception.start),
            ("Iniciar como dentista.", dentist.start),
            ("Atualizar sessão atual.", current_session_manager.update),
            ("Finalizar sessão atual.", current_session_manager.finish),
        ]
    
    MainMenu(clinic, options).run()

def start_application(clinic: Clinic):
    tui.splash(["Bem-vindo ao Dente Clean Manager!", "", "Pressione [Enter] para iniciar uma sessão"])
    main_menu(clinic)
