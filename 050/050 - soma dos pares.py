# Enunciado:

"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""

# Solução:

soma = 0

# Até 7 pois sempre é 1 a mais
for c in range(1, 7):
    num = int(input(f"digite o {c}* número - "))

    # Se for par adiciona à soma final
    if num % 2 == 0:
        soma += num

print(f"A soma dos números pares digitados {soma}")