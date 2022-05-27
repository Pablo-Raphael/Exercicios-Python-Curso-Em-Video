# Enunciado:

"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

# Solução:

num1 = int(input("Digite o primeiro valor desejado - "))
num2 = int(input("Digite o segundo valor desejado - "))

# Se o primeiro for maior que o segundo
if num1 > num2:
    print(f"O número {num1} é MAIOR que o número {num2}")

# Se o segundo for maior que o primeiro
elif num2 > num1:
    print(f"O número {num2} é MAIOR que o número {num1}")

# Se chegar nesse ponto, só pode significar que nenhum dos dois é maior,\
# logo só pode ser igual
else:
    print('Os dois números são IGUAIS')