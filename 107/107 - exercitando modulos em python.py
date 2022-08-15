# Enunciado:

"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

# Solução:

from ex107 import *


print('='*35)

num = float(input('Digite o número : '))
aumente = float(input('Digite quantos % AUMENTAR : '))
diminua = float(input('Digite quantos % DIMINUIR : '))

print('-'*35)

print(f'O dobro é {dobrar(num)}')
print(f'A metade é {metade(num)}')
print(f'{num} + {aumente}% é {aumentar(num, aumente)}')
print(f'{num} - {diminua}% é {diminuir(num, diminua)}')

print('='*35)