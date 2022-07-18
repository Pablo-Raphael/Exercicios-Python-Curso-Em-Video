# Enunciado:

"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

# Solução:


lista = list()

# Adiciona os números do usuário à lista
for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}* valor : ')))

print('='*40)

# O método .index() mostra a posição do valor que lhe é passado
# A função max() mostra o maior valor
maior = max(lista)
posi_maior = lista.index(maior) + 1
print(f'O MAIOR valor foi {maior} na posição {posi_maior}')

# A função min() mostra o menor valor 
menor = min(lista)
posi_menor = lista.index(menor) + 1
print(f'O MENOR valor foi {min(lista)} na posição {posi_menor}')

print('='*40)