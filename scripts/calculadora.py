def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Teste Simples
if __name__ == "__main__":
    print("Calculadora Simples")
    print(f"Soma: 2 + 3 = {soma(2, 3)}")
    print(f"Subtração: 5 - 2 = {subtracao(5, 2)}")
    print(f"Multiplicação: 4 * 3 = {multiplicacao(4, 3)}")
    print(f"Divisão: 10 / 2 = {divisao(10, 2)}")
    print(f"Divisão por zero: 10 / 0 = {divisao(10, 0)}")
