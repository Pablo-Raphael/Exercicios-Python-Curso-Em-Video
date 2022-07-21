# Enunciado:

"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

# Solução:


print('='*40)
print('Digite 0 para encerrar o programa')
print('='*40)

lista = []

while True:
    num = int(input('Digite um número : '))

    if num == 0:
        break

    lista.append(num)

lista.sort(reverse=True)

print('='*40)
print(f'A lista tem {len(lista)} números')
print(f'Em Ordem Decresente : {lista}')

if 5 in lista:
    print('O número 5 ESTÁ a lista')
else:
    print('O número 5 NÃO está na lista')
print('='*40)