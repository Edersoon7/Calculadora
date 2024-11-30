
#!/usr/bin/env python3

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        print("\nEscolha a operação: (+, -, *, /) ou 'sair' para encerrar.")
        operacao = input("Operação: ")

        if operacao == "+":
            print(f"Resultado: {num1 + num2}")
        elif operacao == "-":
            print(f"Resultado: {num1 - num2}")
        elif operacao == "*":
            print(f"Resultado: {num1 * num2}")
        elif operacao == "/":
            print(f"Resultado: {num1 / num2}" if num2 != 0 else "Erro: divisão por zero.")
        elif operacao.lower() == "sair":
            print("Encerrando a calculadora. Até mais!")
            break
        else:
            print("Operação inválida.")

        print("----------------------------------")

calculadora()

