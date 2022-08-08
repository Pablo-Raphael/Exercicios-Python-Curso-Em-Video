# Enunciado:

"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

# Solução:


from random import randint

def sortear(num):
    print('Sorteando 5 valores: ', end='')

    for c in range(0, 5):
        num.append(randint(1, 10))
        print(num[c], end=' ')

    print('FIM')


def somapar(num):
    pares = 0

    for c in num:
        if c % 2 == 0:
            pares += c
            
    print(f'A soma dos pares de {num} é {pares}')


print('='*50)
numeros = []
sortear(numeros)
somapar(numeros)
print('='*50)
