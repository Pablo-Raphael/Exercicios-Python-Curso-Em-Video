# Enunciado:

"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

# Solução:


from ex109 import *


print('='*35)
num = float(input('Digite o número : '))
aumente = float(input('Digite quantos % AUMENTAR : '))
diminua = float(input('Digite quantos % DIMINUIR : '))
mostrar = input('Quer mostar como moeda?[S/N] : ')[0].lower() == 's'

print('-'*35)
print(f'O dobro é {dobrar(num, mostrar)}')
print(f'A metade é {metade(num, mostrar)}')
print(f'{num} + {aumente}% é {aumentar(num, aumente, mostrar)}')
print(f'{num} - {diminua}% é {diminuir(num, diminua, mostrar)}')
print('='*35)