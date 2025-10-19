# nome_organizador.py

# Peça para o usuário colar a lista de nomes, separados por vírgula ou linha
print("Cole sua lista de nomes e pressione Enter duas vezes para finalizar:")

# Ler a lista do usuário
import sys
nomes = []
while True:
    linha = input()
    if linha == "":
        break
    nomes.append(linha.strip())

# Remover duplicatas e ordenar
nomes_unicos = sorted(set(nomes))

# Mostrar o resultado
print("\nLista organizada e sem duplicatas:")
for nome in nomes_unicos:
    print(nome)