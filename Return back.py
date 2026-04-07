import os

os.system("cls")

def somar(num1, num2):
    soma = num1 + num2
    return soma

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = somar(numero1, numero2)
print(f"A soma de {numero1} e {numero2} é: {resultado}")
