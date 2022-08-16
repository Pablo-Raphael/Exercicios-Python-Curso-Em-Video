# Enunciado:

"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
"""

# Solução:


from ex108 import *

print('='*35)
num = float(input('Digite o número : '))
aumente = float(input('Digite quantos % AUMENTAR : '))
diminua = float(input('Digite quantos % DIMINUIR : '))
print('-'*35)

print(f'O dobro é {moeda(dobrar(num))}')
print(f'A metade é {moeda(metade(num))}')
print(f'{moeda(num)} + {aumente}% é {moeda(aumentar(num, aumente))}')
print(f'{moeda(num)} - {diminua}% é {moeda(diminuir(num, diminua))}')
print('='*35)