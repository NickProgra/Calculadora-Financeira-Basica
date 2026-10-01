# 📈 Financial Calculator in Python

An interactive console-based application developed in **Python** to assist with financial calculations and core mathematical operations. The project features a modular architecture, input validation, exception handling, and local data persistence via `.txt` file logging.

---

## 🚀 Features

- **Simple Interest:** Calculates accumulated interest and total amount based on principal, rate, and time.
- **Compound Interest:** Calculates compound returns over time for investment or loan analysis.
- **Cash Discount:** Applies percentage discounts to initial price values.
- **Percentage Increase:** Adds percentage markups to a base price or value.
- **Basic Arithmetic Operations:** Addition, subtraction, multiplication, and division (with built-in division-by-zero protection).
- **Operation History:** Saves and reads calculation logs from a persistent file (`historico.txt`).
- **Data Management:** Option to clear and permanently wipe the saved operation history.

---

## 🛠️ Technologies & Concepts Applied

- **Python 3.x**
- **Control Flow:** `while` loops for continuous menu navigation and decision-making via `if/elif/else`.
- **Modular Design:** Business logic encapsulated into dedicated reusable functions (`def`).
- **Exception Handling:** `try/except` blocks preventing application crashes from invalid user inputs (`ValueError`).
- **File I/O:** Reading (`r`), appending (`a`), and file management using the native `os` module.
- **Python Best Practices:** Execution flow controlled via `if __name__ == "__main__":`.

---

## 📋 Structure & Function Overview

### 1. Persistence & System Module
* `salvar_no_historico(texto)`: Receives a formatted summary string and appends a new entry to `historico.txt`.
* `exibir_historico()`: Reads `historico.txt` line by line and displays formatted logs in the console.
* `limpar_historico()`: Checks for `historico.txt` using the `os` library and deletes it from the disk.
* `pedir_numero_positivo(mensagem)`: Utility function with a validation loop to enforce strictly positive numeric inputs.

### 2. Financial Calculation Module
* `calcular_juros_simples(capital, taxa, tempo)`: Applies $J = C \times i \times t$ and returns interest and final amount.
* `calcular_juros_compostos(capital, taxa, tempo)`: Applies $M = C \times (1 + i)^t$ and returns accrued interest and final total.
* `calcular_desconto(preco, porcentagem)`: Calculates discount amount and final discounted price.
* `calcular_acrescimo(preco, porcentagem)`: Calculates price increase amount and updated total price.

### 3. Arithmetic Operations Module
* `somar(valor1, valor2)`: Returns the sum of two values.
* `subtrair(valor1, valor2)`: Returns the difference between two values.
* `multiplicar(valor1, valor2)`: Returns the product of two values.
* `dividir(valor1, valor2)`: Returns the division result, with validation against division by zero.

### 4. Application Control
* `menu_principal()`: Handles the user interface, interactive menu options, input collection, and overall flow control.

---

## 📦 How to Run

1. Ensure you have **Python 3.x** installed.
2. Clone this repository or download the source script:
   ```bash
   git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
