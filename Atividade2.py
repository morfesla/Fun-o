def calcular_estatisticas(lista_numeros):
    """Processa todos os cálculos matemáticos solicitados."""
    pares = [n for n in lista_numeros if n % 2 == 0]
    impares = [n for n in lista_numeros if n % 2 != 0]
    positivos = [n for n in lista_numeros if n > 0]
    negativos = [n for n in lista_numeros if n < 0]

    # Dicionário para organizar os resultados
    stats = {
        "qtd_pares": len(pares),
        "qtd_impares": len(impares),
        "qtd_positivos": len(positivos),
        "qtd_negativos": len(negativos),
        "maior": max(lista_numeros),
        "menor": min(lista_numeros),
        "media_pares": sum(pares) / len(pares) if pares else 0,
        "media_impares": sum(impares) / len(impares) if impares else 0,
        "media_geral": sum(lista_numeros) / len(lista_numeros)
    }
    return stats

def exibir_resultados(numeros, s):
    """Cuida apenas da parte visual/saída de dados."""
    print("\n" + "="*35)
    print(f"{' RESULTADOS ':^35}")
    print("="*35)
    print(f"Total de números: {len(numeros)}")
    print(f"Pares: {s['qtd_pares']} | Ímpares: {s['qtd_impares']}")
    print(f"Positivos: {s['qtd_positivos']} | Negativos: {s['qtd_negativos']}")
    print(f"Maior: {s['maior']} | Menor: {s['menor']}")
    print(f"Média Pares: {s['media_pares']:.2f}")
    print(f"Média Ímpares: {s['media_impares']:.2f}")
    print(f"Média Geral: {s['media_geral']:.2f}")
    print(f"Ordem Inversa: {numeros[::-1]}")
    print("="*35)

def principal():
    """Função mestre que coordena o programa."""
    lista_entrada = []
    for i in range(1, 6):
        while True: # Garante que o usuário digite um número válido
            try:
                n = int(input(f"Digite o {i}º número inteiro: "))
                lista_entrada.append(n)
                break
            except ValueError:
                print("Erro! Por favor, digite um número inteiro válido.")

    # Chama as funções especialistas
    dados_processados = calcular_estatisticas(lista_entrada)
    exibir_resultados(lista_entrada, dados_processados)

# Executa o programa
if __name__ == "__main__":
    principal()