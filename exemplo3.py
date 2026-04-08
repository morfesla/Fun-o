import os
#função
def logo_senai():
    os.system("cls")
    print("====== ======")
    print("    SENAI     ")
    print("====== ======")

#Função com retorno
logo_senai()
print("========= SOLICITANDO DADOS ===========")
n1 = int(input("Digite um numero:" ))
n2 = int(input("Digite o segundo numero:"))

def multiplicar(a,b):
    multiplicacao = a * b
    print(f"Multiplicacao: {multiplicacao}")

def divisao(a, b):
    dividir = a / b
    print(f"divisao: {dividir}")

def  somar(a,b):
     return a + b

def subtracao(a, b):
    return a - b

logo_senai()
soma = n1 + n2
subtracao = n1 - n2
multiplicao = n1 * n2
print("-------- MOSTRANDO DADOS --------")
print(f"Subtração {subtracao}")
print(f"soma: {soma}")
multiplicar(n1, n2)
divisao(n1, n2)