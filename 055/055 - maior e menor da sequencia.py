# Enunciado:

"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""

# Solução:


maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f"Qual o peso da {pessoa}a pessoa? - "))
    # Na primeira coleta, tanto o maior quanto o menor peso são o peso da primeira pessoa
    if pessoa == 1:
        maior = peso
        menor = peso
    # Caso a primeira coleta já tenha sido feita, os novos valores serão atualizados\
    # caso ultrapassem o maior ou menor peso.
    else:
        # Se o peso da pessoa da vez for maior que o último maior peso
        if peso > maior:
            maior = peso
        
        # Se o peso da pessoa da vez for menor que o último menor peso
        if peso < menor:
            menor = peso

print(f"O maior é {maior} e o menor é {menor}")