# TODO: remove this, not needed anymore

from menus.interface import MainMenu

from .use_cases import session_manager
from .reception import reception


__all__ = ["reception"]


class SomeModel:
    pass


def start_reception(model: SomeModel):
    while session_manager.register(reception.model, dry_run=True, should_update=True):
        pass

    reception.run()


startup = MainMenu(SomeModel(), [("Iniciar como recepção.", start_reception)])
