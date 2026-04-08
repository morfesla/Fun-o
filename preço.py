import os

os.system("cls")

def calcular_inflação(preço):
    if preço < 100:
       novo_preço * 1.10
    else:
        novo_preço = preço * 1.20
    return novo_preço

preço_inicial = float(input("digite seu preço inicial: "))
preço_final = calcular_inflação(preço_inicial)

print(f"O preço inflacionado é R$: {preço_final: 2f}")