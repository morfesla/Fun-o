import os

os.system('cls' if os.name == 'nt' else 'clear')

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = calcular_idade(ano_nascimento, ano_atual)
print(f"Sua idade é: {idade} anos.")
