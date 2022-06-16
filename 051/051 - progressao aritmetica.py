# Enunciado:

"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
o final, mostre os 10 primeiros termos dessa progressão.
"""

# Solução:


num = int(input('Digite o valor inicial = '))
razao = int(input('Agora digite a razão = '))

# 10 vezes mostrado
for c in range(0, 10):
    # Altera o comportamento do 'print' para o próximo continuar na mesma linha 
    print(num, end=' > ')

    # Aumenta o número atual da progressão com base na razão
    num += razao

print('fim')

