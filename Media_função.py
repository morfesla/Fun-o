import os

os.system("cls")


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
def verificar_aprovacao(media):
    if media >= 7:
        print(f"A média é {media}. Aluno aprovado!")
    else:
        print(f"A média é {media}. Aluno reprovado.")
print("Digite as notas do aluno:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = calcular_media(nota1, nota2)
verificar_aprovacao(media)