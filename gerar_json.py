import json

def letra_para_numero(letra):
    return ord(letra.upper()) - 65

def numero_para_letra(num):
    return chr((num % 26) + 65)

def calcular_diferenca(letra1, letra2):
    return (letra_para_numero(letra2) - letra_para_numero(letra1)) % 26

def gerar_nomes_semelhantes(input_str, lista):
    resultados = []
    input_str = input_str.upper()

    for nome in lista:
        nome_upper = nome["nome"].upper()
        if len(nome_upper) < len(input_str):
            continue

        soma_dif = 0
        valido = True

        for i in range(len(input_str)):
            dif = calcular_diferenca(input_str[i], nome_upper[i])
            # garante que a diferença é sempre pra frente, cerca de 6 ou 7 letras
            if dif not in [6, 7]:
                valido = False
                break
            soma_dif += dif

        if valido:
            resultados.append((soma_dif, nome["nome"]))

    # pega os 9 mais compatíveis e retorna só os nomes
    melhores = [nome for _, nome in sorted(resultados, key=lambda x: x[0])[:9]]
    return melhores


# === Exemplo de uso ===
with open("/Users/arthuralves/Documents/nomes.json", "r", encoding="utf-8") as f:
    lista = json.load(f)

entrada = input("Digite as letras: ")
nomes_compativeis = gerar_nomes_semelhantes(entrada, lista)

print("\nNomes compatíveis:")
for nome in nomes_compativeis:
    print(nome)