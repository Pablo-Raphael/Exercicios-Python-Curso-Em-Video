# Enunciado:

"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

# Solução:


lista = [[], [], []]

somapar = somaterceira = 0

for linha in range(len(lista)):
    for coluna in range(0, 3):
        lista[linha].append(int(input(f'Digite o Numero [ {linha} / {coluna} ] ')))

print('-'*40)

for linha in lista:
    for numero in linha:
        print('[{:^5}]'.format(numero), end=' ')
        if numero % 2 == 0:
            somapar += numero
        if linha == lista[2]:
            somaterceira += numero
    print()

print('-'*40)

print(f'A soma dos números pares é {somapar}')
print(f'A soma da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda coluna é {max(lista[1])}')