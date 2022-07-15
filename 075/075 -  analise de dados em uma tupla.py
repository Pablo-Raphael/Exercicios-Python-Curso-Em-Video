# Enunciado:

"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

# Solução:

pares = []

tupla = (
    int(input('Digite o primeiro valor ')),
    int(input('Digite outro valor ')),
    int(input('Digite outro valor ')),
    int(input('Digite o último valor ')),
)

print(f'Os números foram: {tupla}')

print(f'O número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O primeiro 3 aparece na {tupla.index(3)+1}* posição')
else:
    print('O número 3 não foi digitado')

print("Os números pares foram - ", end="")
for num in tupla:
    if num % 2 == 0:
        print(num, end=" ")

print("(Fim)")