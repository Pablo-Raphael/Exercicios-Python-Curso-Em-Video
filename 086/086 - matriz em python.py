# Enunciado:

"""
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

# Solução:

lista = [[], [], []]

# 3 linhas
for linha in range(3):
    # 3 colunas
    for coluna in range(0, 3):
        lista[linha].append(int(input(f'Digite o Numero [ {linha} / {coluna} ] ')))


print('='*40)

for linha in lista:
    for numero in linha:
        print('[{:^5}]'.format(numero), end=' ')
    print()

print('='*40)