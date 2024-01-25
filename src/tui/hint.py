from tui._screen import Screen
from tui._utils import normalize_lines


def info(content: str | list[str] | Exception) -> None:
    """Imprime uma tela do tipo ``hint`` para informações"""
    symbol = "⌾"  # unicode: 233E
    _hint(symbol, content)


def warn(content: str | list[str] | Exception) -> None:
    """Imprime uma tela do tipo ``hint`` para avisos"""
    symbol = "⚠"  # unicode: 26A0
    _hint(symbol, content)


def _hint(symbol: str, content: str | list[str] | Exception) -> None:
    """Define uma tela de avisos.

    Será posto um símbolo de aviso ao início e uma mensagem de proseguir ao fim.

    Arguments
    ---------
    symbol: str
        O símbolo que será usado na primeira linha do conteúdo.
    content: str | list[str] | Exception
        Recebe ``content`` para imprimí-lo na tela.
        Esse argumento é automaticamente convertido para o tipo ``list[str]``.

    Example
        -------
        >>> hint("*", "Paciente não pode ser registrado!")
        +-------------------------------------------------------+
        |                                                       |
        |                                                       |
        |        [*] Paciente não pode ser registrado! [*]      |
        |                                                       |
        |           Pressione [Enter] para continuar.           |
        |                                                       |
        |                                                       |
        +-------------------------------------------------------+
    """

    # Defnie funções internas
    def to_list_str(content: str | list[str] | Exception) -> list[str]:
        """Converte ``content`` para o tipo correto"""
        match content:
            case str():  # põe ``content`` dentro de uma lista
                return [content]
            case Exception():  # converte ``Exception.args`` para lista
                return list(content.args)  # note que args é do tipo ``tuple``
            case _:
                return content

    # Inicio da função principal
    screen = Screen()

    # Corrige o tipo de content e,
    content = to_list_str(content)

    # Adiciona símbolo de aviso ao início
    content[0] = f"{symbol}  {content[0]} {symbol}"

    # Adiciona mensagem para continuar ao fim
    content += ["", "Pressione [Enter] para continuar"]

    content = normalize_lines(content, screen.width - 4)

    # Renderiza a tela e espera por entrada.
    screen.render_full_screen(content, center=True)
    screen.wait()
