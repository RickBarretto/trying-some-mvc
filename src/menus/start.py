import tui

from .reception import reception

__all__ = ["reception"]

class SomeModel:
    pass

def start_reception(model: SomeModel):
    try:
        date = tui.Prompt.get_date("Insira a data da sessão atual.")
    except ValueError as e:
        tui.WarningScreen(e).render()
        return

    reception.controller.update_current_session(date)
    reception.run()


startup = tui.MainMenu(
    SomeModel(), [(start_reception, "Iniciar como recepção.")]
)
