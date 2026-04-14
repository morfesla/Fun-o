import os

os.system('cls' if os.name == 'nt' else 'clear')

def calcular_media(n1   , n2):
    media = (n1 + n2) / 2
    return media

def verficar_situação(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado
    
print("Solicitando Dados do Aluno")

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = calcular_media(primeira_nota, segunda_nota)
situacao = verficar_situação(media)

print(f"A média do aluno é: {media:.2f}")
print(f"A situação do aluno é: {situacao}")