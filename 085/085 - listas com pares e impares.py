# Enunciado:

"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""

# Solução:


lista = [[], []]

for posi in range(1, 8):

    num = int(input(f'Digite o {posi}o número : '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print('='*50)
print(f'Os PARES foram : {sorted(lista[0])}')
print(f'Os ÍMPARES foram : {sorted(lista[1])}')
print('='*50)