# Enunciado:

"""
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""

# Solução:

num = quant = 0

while True:
    novo_num = int(input('Digite o número (999 para interromper) - '))

    # Se digitou 999 para imediatamente o while
    if novo_num == 999:
        break

    num += novo_num
    quant += 1

print(f'Digitou {quant} números e a soma entre eles: {num}')
