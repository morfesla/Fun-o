import os

os.system("cls")

def inteiro_positivo(numero):
    if numero > 0:
        print(f"O número {numero} é positivo.")
    else:
        print(f"O número {numero} é negativo ou zero.")

numero1 = int(input("Digite um número: "))
inteiro_positivo(numero1)
