# Enunciado:

"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

# Solução:


lista = list()

maior = menor = 0

for c in range(0, 5):

    num = int(input('Digite um número : '))

    if c == 0 or num > lista[-1]:
        lista.append(num)
        maior = menor = num

    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao += 1
            
print(lista)