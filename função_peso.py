import os

os.system("cls")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    match True:
        case _ if imc < 18.5:
            return "Abaixo do peso"
        case _ if imc <= 24.9:
            return "Peso normal"
        case _ if imc <= 29.9:
            return "Sobrepeso"
        case _ if imc <= 34.9:
            return "Obesidade grau 1"
        case _ if imc <= 39.9:
            return "Obesidade grau 2"
        case _:
            return "Obesidade grau 3"


def main():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")


main()  