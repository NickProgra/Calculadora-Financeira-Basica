# 📈 Calculadora Financeira em Python

Uma aplicação interativa de console desenvolvida em **Python** para auxílio em cálculos financeiros e operações matemáticas essenciais. O projeto conta com arquitetura modular, validações de entrada, tratamento de exceções e persistência de dados local em arquivo `.txt`.

---

## 🚀 Funcionalidades

- **Juros Simples:** Cálculo do montante e juros acumulados com base em capital, taxa e tempo.
- **Juros Compostos:** Cálculo de rendimento com juros sobre juros para análises de investimentos ou empréstimos.
- **Desconto à Vista:** Aplicação de porcentagens de desconto sobre o valor inicial.
- **Acréscimo Percentual:** Aumento percentual sobre um preço ou valor de referência.
- **Operações Aritméticas Básicas:** Soma, subtração, multiplicação e divisão (com proteção contra divisão por zero).
- **Histórico de Operações:** Leitura e gravação de relatórios de cálculos em disco rígido (`historico.txt`).
- **Gestão de Dados:** Opção para exclusão e limpeza completa do histórico armazenado.

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Python 3.x**
- **Estruturas de Controle:** Loops (`while`) para execução contínua do menu e seleções (`if/elif/else`).
- **Modularização:** Encapsulamento de regras de negócio em funções exclusivas (`def`).
- **Tratamento de Exceções:** Blocos `try/except` para impedir falhas de execução por entradas inválidas de dados (`ValueError`).
- **Manipulação de Arquivos (I/O):** Leitura (`r`), gravação (`a`) e manipulação de arquivos no sistema operacional via módulo nativo `os`.
- **Boas Práticas de Código:** Utilização da convenção `if __name__ == "__main__":` para controle de fluxo de execução.

---

## 📋 Estrutura e Explicação das Funções

### 1. Módulo de Persistência e Sistema
* `salvar_no_historico(texto)`: Recebe uma string formatada contendo o resumo da operação realizada e grava uma nova linha no arquivo `historico.txt`.
* `exibir_historico()`: Abre o arquivo `historico.txt`, realiza a leitura linha a linha e exibe os registros formatados no console.
* `limpar_historico()`: Verifica a existência do arquivo `historico.txt` através da biblioteca `os` e o remove do sistema.
* `pedir_numero_positivo(mensagem)`: Função utilitária com loop de validação que garante o recebimento de valores numéricos estritamente maiores que zero.

### 2. Módulo de Cálculos Financeiros
* `calcular_juros_simples(capital, taxa, tempo)`: Aplica a fórmula $J = C \times i \times t$ e retorna os juros e o montante final.
* `calcular_juros_compostos(capital, taxa, tempo)`: Aplica a fórmula $M = C \times (1 + i)^t$ e retorna os juros acumulados e o montante final.
* `calcular_desconto(preco, porcentagem)`: Calcula o abatimento e o valor final com desconto.
* `calcular_acrescimo(preco, porcentagem)`: Calcula o valor do acréscimo e o valor final atualizado.

### 3. Módulo de Operações Aritméticas
* `somar(valor1, valor2)`: Retorna a adição entre dois valores.
* `subtrair(valor1, valor2)`: Retorna a diferença entre dois valores.
* `multiplicar(valor1, valor2)`: Retorna o produto entre dois valores.
* `dividir(valor1, valor2)`: Retorna a divisão de dois valores, contendo validação interna para evitar divisão por zero.

### 4. Controle da Aplicação
* `menu_principal()`: Gerencia a interface de usuário, exibição do menu interativo, captura de seleções e direcionamento do fluxo do programa.

---

## 📦 Como Executar o Projeto

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `.py`:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
