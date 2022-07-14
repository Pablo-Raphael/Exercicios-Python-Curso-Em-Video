# Enunciado:

"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

# Solução:

from random import randint

num = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print('Os números foram: ', end='')
for n in num:
    print(n, end=' ')

print()
print(f'O maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')