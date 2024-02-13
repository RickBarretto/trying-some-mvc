===========
Dente Clean
===========

Dente clean é uma aplicação para gerenciamento de uma clínica odontológica,
onde o usuário poderá cadastrar pacientes para uma clínica e realizar consultas.

Execução
========

Para executar código como usuário:

        $ py src/main.py        # windows
        $ python src/main.py    # linux


Para executar o código como desenvolvedor, 
ou seja, com o povoamento já feito:

        $ py src/dev.py        # windows
        $ python src/dev.py    # linux


Estrutura e Explicação
======================

Entity
------

``entity`` é o pacote onde estão localizados os moldes da aplicação 
e suas entidades: ``Clinic``, ``Patient``s, ``Session``s.

Essas entidades possuem pouca ou nenhuma lógica e foram feitas para serem
manipuladas pelas funções do ``app``.

TUI
---

'TUI' significa 'Text-based User Interface'. ``tui`` o pacote responsável por
imprimir o conteúdo na tela do usuário, assim como receber entradas do mesmo.

Dispõe-se de vários tipos de menus, cada um com sua própria especificidade.

App
---

``app`` é o pacote responsável pelos casos de uso da aplicação, responsável por
negociar com os pacotes de ``Entity`` e ``TUI``.

Esse pacote é o maior e mais complexo, e é dividido entre alguns módulos
e um subpacote chamado de ``app.use_cases``.

Dentre seus módulos, temos ``app.dentist``, ``app.reception``
que definem a implementação dos menus de aplicação, dentista e recepção, 
respectivamente.
E ``app.menu`` que define uma classe base usada pelas implementações acima.

Use Cases
~~~~~~~~~

``app.use_cases`` é responsável por definir os casos de uso da aplicação.
Basicamente, toda a lógica e regra de negócios usada na aplicação ou 
dentro dos menus de usuário.

Temos suas aplicações divididas em três grandes grupos de gerência:
* ``app.use_cases.current_session_manager`` para gerência da sessão atual,
* ``app.use_cases.session_manager`` para gerência da sessões em geral e
* ``app.use_cases.patients_manager`` para gerência de pacientes.

Casos de uso menores e que se repetem dentro dos principais 
estão presentes em ``app.use_cases.commons``.

Lembrando que muitas vezes os casos de uso podem chamar outros
para uma experiência mais fluida do usuário.