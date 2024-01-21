from singletons.reception import reception
import screen


__all__ = ["reception"]


class ControllerPlaceholder:
    pass


def start_reception(controller: ControllerPlaceholder):
    try:
        date = screen.Prompt.get_date("Insira a data da sessão atual.")
    except ValueError as e:
        screen.WarningScreen(e).render()
        return

    reception.controller.update_current_session(date)
    reception.run()


startup = screen.MainMenu(
    ControllerPlaceholder(), [(start_reception, "Iniciar como recepção.")]
)
