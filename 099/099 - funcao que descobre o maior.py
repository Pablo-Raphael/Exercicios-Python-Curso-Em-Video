# Enunciado:

"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

# Solução:


def maiornum(*numeros):
    for numero in numeros:
        print(numero, end=' ')

    print(f'Foram {len(numeros)} números ao todo')

    maior = max(numeros)

    print(f'O maior dentre eles é {maior}')

    print('-' * 50)


print('='*50)
print('MAIOR NÚMERO')
print('='*50)

maiornum(1, 2, 3, 4, 5, 6)
maiornum(1, 2, 3, 4, 5)
maiornum(1, 2, 3, 4)
maiornum(1, 2, 3)