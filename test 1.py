import os

def salvar_no_historico(texto):
    """Guarda uma nova linha no ficheiro historico.txt"""
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")

def exibir_historico():
    """lê e exibe todas as linhas gravadas no ficheiro"""
    print("\n--- HISTÓRICO DE OPERAÇÕES (SALVO EM DISCO) ---")
    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) == 0:
                print("Nenhuma operação registrada no ficheiro.")
            else:
                for i, linha in enumerate(linhas, 1):
                    print(f"{i}. {linha.strip()}")
    except FileNotFoundError:
        print("Nenhum ficheiro de histórico encontrado ainda.")

def limpar_historico():
    """Apaga o ficheiro de historico do computador"""
    if os.path.exists("historico.txt"):
        os.remove("historico.txt")
        print("\n[SUCESSO] Historico de operações apagado com sucesso!")
    else:
        print("\n[AVISO] Não existe histórico para ser apagado.")

def pedir_numero_positivo(mensagem):
    """Pede um número e garante que ele seja maior que zero."""
    valor = -1.0
    while valor <= 0:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("[ERROR] Por favor, digite um valor maior que zero!")
        except ValueError:
            print("[ERROR] Entrada Inválida! Digite apenas números.")
    return valor


def calcular_juros_simples(capital, taxa, tempo):
    juros = capital * (taxa / 100) * tempo
    total = capital + juros
    return juros, total

def calcular_desconto(preco,porcentagem):
    valor_desconto = preco * (porcentagem / 100)
    preco_final = preco - valor_desconto
    return valor_desconto, preco_final

def calcular_acrescimo(preco,porcentagem):
    valor_acrescimo = preco * (porcentagem / 100)
    preco_final = preco + valor_acrescimo
    return valor_acrescimo, preco_final

def soma (v1, v2):
    return v1 + v2

def subtracao (v1, v2):
    return v1 - v2

def multiplicacao (v1, v2):
    return v1 * v2

def divisao (v1, v2):
    if v2 == 0:
        return none
    return v1 / v2

def calcular_juros_compostos (capital, taxa, tempo):
    total = capital * ((1 + (taxa / 100)) ** tempo)
    juros = total - capital
    return juros, total

def menu_principal():
    opcao = -1


    while opcao != 0:
        print("\n=== CALCULADORA FINANCEIRA ===")
        print("1 - Calcular Juros Simples")
        print("2 - Calcular Juros Compostos")
        print("3 - Calcular Desconto á Vista")
        print("4 - Calcular Acrescimo")
        print("5 - Soma")
        print("6 - Subtração")
        print("7 - Multiplicação")
        print("8 - Divisão")
        print("9 - Ver Histórico de Operações")
        print("10 - Limpar histórico")
        print("0 - Sair")

        try:
            opcao = int(input("Escolhauma opção: "))

            if opcao == 1:
                capital = float(input("Digite o valor inicial (R$): "))
                taxa = float(input("Digite a taxa de juros anual (%): "))
                tempo = int(input("Digite o tempo em anos: "))

                juros, total = calcular_juros_simples(capital, taxa, tempo)

                resumo = f"Juros Simples: Capital R$ {capital:.2f} | Juros: R$ {juros:.2f} | Total: R$ {total:.2f}"
                salvar_no_historico(resumo)
            
                print(f"O valor dos juros é: R$ {juros:.2f}")
                print(f"O montante total final é: R$ {total:.2f}")
 
            elif opcao == 2:
                capital = float(input("Digite o valor inicial (R$): "))
                taxa = float(input("Digite a taxa de juros por período (%): "))
                tempo = int(input("Digite o tempo em períodos (meses/anos): "))

                juros, total = calcular_juros_compostos(capital, taxa, tempo)

                resumo = f"Juros Compostos: Capital R$ {capital:.2f} | Juros: R$ {juros:.2f} | Total: R$ {total:.2f}"
                salvar_no_historico(resumo)

                print(f"O valor dos juros acumulados é: R$ {juros:.2f}")
                print(f"O montante total final é: R$ {total:.2f}")

            elif opcao == 3:
                preco = float(input("Digite o preço original do produto (R$): "))
                desconto = float(input("Digite a porcentagem de desconto (%): "))

                valor_desconto, preco_final = calcular_desconto(preco, desconto)

                resumo= f"Desconto: Preço R$ {preco:.2f} | Desconto: R$ {valor_desconto:.2f} | Final: R$ {preco_final:.2f}"
                salvar_no_historico(resumo)
            
                print(f"Valor do desconto: R$ {valor_desconto:.2f}")
                print(f"Preço final com desconto: R$ {preco_final:.2f}")

            elif opcao == 4:
                preco = float(input("Digite o preço inicial (R$): "))
                acrescimo = float(input("Digite a porcentagem que ira aumentar (%): "))

                valor_acrescimo, preco_final = calcular_acrescimo(preco, acrescimo)

                resumo = f"Acréscimo: Preço R$ {preco:.2f} | Aumento: R$ {valor_acrescimo:.2f} | Final: R$ {preco_final:.2f}"
                salvar_no_historico(resumo)
            
                print(f"Valor do acrescimo: R$ {valor_acrescimo:.2f}")
                print(f"Preço final com acrescimo: R$ {preco_final:.2f}")

            elif opcao == 5:
                v1 = float(input("Digite o primeiro valor (R$): "))
                v2 = float(input("Digite o segundo valor (R$): "))

                resultado = soma(v1, v2)

                resumo = f"Soma: R$ {v1:.2f} + R$ {v2:.2f} = R$ {resultado:.2f}"
                salvar_no_historico(resumo)

                print(f"O resultado da soma é: R$ {resultado:.2f}")

            elif opcao == 6:
                v1 = float(input("Digite o primeiro valor (R$): "))
                v2 = float(input("Digite o segundo valor (R$): "))

                resultado = subtracao(v1, v2)

                resumo = f"Subtração: R$ {v1:.2f} - R$ {v2:.2f} = R$ {resultado:.2f}"
                salvar_no_historico(resumo)

                print(f"O resultado da Subtração é: R$ {resultado:.2f}")

            elif opcao == 7:
                 v1 = float(input("Digite o primeiro valor (R$): "))
                 v2 = float(input("Digite o segundo valor (R$): "))

                 resultado = multiplicacao(v1, v2)

                 resumo = f"Multiplicação: R$ {v1:.2f} * R$ {v2:.2f} = R$ {resultado:.2f}"
                 salvar_no_historico(resumo)

                 print(f"O resultado da Multiplicação é: R$ {resultado:.2f}")
                
            elif opcao == 8:
                 v1 = float(input("Digite o primeiro valor (R$): "))
                 v2 = float(input("Digite o segundo valor (R$): "))

                 resultado = divisao(v1, v2)

                 resumo = f"Dividir: R$ {v1:.2f} / R$ {v2:.2f} = R$ {resultado:.2f}"
                 salvar_no_historico(resumo)

                 print(f"O resultado da Divisão é: R$ {resultado:.2f}")
                
            elif opcao == 9:
                exibir_historico()

            elif opcao == 10:
                limpar_historico()
        
            elif opcao == 0:
                print("Obrigado por usar a Calculadora Financeira! Encerrando...")
    
            else:
                print("Opção inválida! Tente novamente.")
                
        except ValueError:
            print("\n[ERRO] Entrada inválida! Por favor, digite apenas números.")
             
if __name__== "__main__":
    menu_principal()
