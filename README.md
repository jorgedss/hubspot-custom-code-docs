# HubSpot Custom Code Snippets

## Objetivo

Este repositório armazena funções e integrações reutilizáveis para HubSpot com o objetivo de acelerar a produtividade.

O intuito é servir como uma biblioteca de "snippets" para copiar e colar diretamente em Ações de Código Personalizado (Custom Code Actions) em workflows.

## Estrutura do projeto

O projeto é organizado por linguagem de programação e, dentro de cada linguagem, por tipo de função. A estrutura principal é a seguinte:

```
/
|-- /js                     # Contém todas as funções e lógicas em JavaScript.
|   |-- /integrations       # Possui pastas para cada integração específica.
|   |-- /utils              # Funções utilitárias comuns para JavaScript.
|-- /python                 # Contém todas as funções e lógicas em Python.
|   |-- /integrations       # Possui pastas para cada integração específica (ex: Intellisign).
|   |-- /utils              # Funções utilitárias comuns para Python (ex: interagir com a API do HubSpot).
|   `-- requirements.txt    # Dependências de pacotes Python.
|

```

## Detalhes das pastas

Este repositório está organizado em duas categorias principais:

- **/integrations**: Contém módulos para integrações específicas com plataformas de terceiros. Cada plataforma (ex: `intellisign`) possui sua própria pasta contendo as funções relevantes para interagir com a API correspondente.
- **/utils**: Contém funções utilitárias, tanto para operações comuns da API do HubSpot (como buscar objetos associados ou propriedades) quanto para tarefas genéricas (como baixar arquivos de URLs).

## Como Usar

1.  **Copiar:** Identifique a função necessária e copie o código do arquivo `.py` correspondente.
2.  **Colar:** Cole o código na sua Ação de Código Personalizado (Custom Code Action) do HubSpot ou no seu ambiente.
3.  Cada arquivo de função é auto documentado. No topo de cada script, você encontrará uma descrição clara sobre:
    - O que a função faz.
    - Quais parâmetros ela espera receber.
    - O que ela retorna após a execução.
    - Instruções básicas ou exemplos de uso.
4.  **Dependências:** Certifique-se de que as bibliotecas listadas em `requirements.txt` (como `requests`) estejam disponíveis no ambiente de execução. (Para Ações de Código Personalizado nativas do HubSpot, `requests` já está incluído).
5.  **Variáveis de Ambiente:** Funções que necessitam de chaves de API (como as da Intellisign ou HubSpot) são projetadas para receber essas chaves como parâmetros, que devem ser gerenciados de forma segura (ex: via "Secrets" no HubSpot).
