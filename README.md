# Projeto: Orientador de carreiras

Este projeto é um sistema de linha de comando desenvolvido em Python que simula uma ferramenta inteligente de orientação de carreiras. Ele utiliza princípios de Programação Orientada a Objetos para analisar o perfil de competências de um usuário e recomendar carreiras futuras.

## Descrição do projeto e propósito

O foco da proposta é conectar lógica de programação e a automação ao desenvolvimento humano e profissional. O sistema permite que um usuário cadastre seu perfil e seus níveis em diversas competências (ex: lógica, colaboração, python). Com base nessas informações, a aplicação gera recomendações personalizadas indicando carreiras e áreas de aprimoramento.

## Estrutura de arquivos e classes

O projeto é organizado de forma modular para separar responsabilidades:

-   **`main.py`**: Ponto de entrada da aplicação. Controla o menu e o fluxo do usuário.
-   **`perfil.py`**: Contém a classe `Perfil`, que modela os dados do usuário e suas competências (armazenadas em um dicionário).
-   **`carreira.py`**: Contém a classe `Carreira`, que modela uma profissão e seus requisitos (também em um dicionário).
-   **`database.py`**: Instancia e armazena (em uma lista) todos os objetos `Carreira` disponíveis no sistema.
-   **`engine.py`**: Contém as funções e condicionais para comparar um objeto `Perfil` com a lista de objetos `Carreira` e gerar a pontuação de "match".

## Competências utilizadas

Para que o sistema funcione, o usuário deve cadastrar seu nível (1-5) nas competências abaixo. **É importante usar exatamente estes nomes** ao criar seu perfil:

-   `lógica`
-   `python`
-   `estatística`
-   `colaboração`
-   `criatividade`
-   `empatia`
-   `liderança`
-   `comunicação`

## Instruções de execução

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório:
    ```bash
    git clone https://github.com/sakkj/GS2_Py
    ```
3.  Navegue até a pasta do projeto:
    ```bash
    cd GS2_Py
    ```
4.  Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```
5.  Siga as instruções no terminal para criar seu perfil. Quando solicitado o "Nome da competência", utilize um dos nomes da lista de "Competências Utilizadas" acima.

## Alunos do grupo

1.    Felipe Hui Hattori - RM:565169

2.    Lucas Kenzo - RM:561325

3.    Rafael Vaz de Lima - RM:566429





