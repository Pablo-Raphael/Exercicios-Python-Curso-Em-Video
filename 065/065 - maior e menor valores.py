# Enunciado:

"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

# Solução:


resp = 'S'
num = quant = soma = maior = menor = 0

while resp == 'S':
    num = int(input('Digite um valor - '))

    # Adiciona o número à soma dos valores e incrementa o contador de somas feitas
    quant += 1
    soma += num

    # Se for a primeira inserção, tanto o maior quanto o menor valor serão os digitados
    if quant == 1:
        maior = menor = num

    else:
        # Se o número inserido for maior que o maior atual, o maior atual será o número inserido
        if num > maior:
            maior = num

        # Se o número inserido for menor que o menor atual, o menor atual será o número inserido
        elif num < menor:
            menor = num

    # Pega apenas a primeira letra do que o usário digitou e a põe em maiúsculo
    resp = input("Quer continuar? [S / N] - ").strip()[0].upper()

print("=-" * 25)
# o trecho :.2f faz com que o número mostrado só tenha 2 casas decimais
print(f"Você digitou {quant} números, a média é {soma/quant:.2f}")
print(f"O maior valor é {maior} e o menor é {menor}")
print("=-" * 25)