# Enunciado:

"""
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

# Solução:

soma = 0

# Para cada número num intervalo de 1 a 500 pulando de 2 em 2 (1, 3, 5, 7...)
for numero in range(1, 501, 2):
    # Se o número for divisível por 3 o número será somado ao total
    if numero % 3 == 0:
        soma += numero

print(soma)