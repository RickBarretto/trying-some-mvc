from singletons.reception import reception
import tui


__all__ = ["reception"]


class ControllerPlaceholder:
    pass


def start_reception(controller: ControllerPlaceholder):
    try:
        date = tui.Prompt.get_date("Insira a data da sessão atual.")
    except ValueError as e:
        tui.WarningScreen(e).render()
        return

    reception.controller.update_current_session(date)
    reception.run()


startup = tui.MainMenu(
    ControllerPlaceholder(), [(start_reception, "Iniciar como recepção.")]
)
