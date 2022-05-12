# Enunciado:

"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# Solução:


# Importa a função que sorteia um número inteiro
from random import randint

# Sorteia o número com a função importada e o guarda
num = randint(1, 5)

# Recebe o palpite do usuário
palpite = int(input('Qual o número que você acha que é? '))


# Se o palpite estiver certo mostrará a mensagem de sucesso
if num == palpite:
    print("=-"*25)
    print("PARABÊNS CAMPEÃO, VOCÊ ACERTOU")
    print("=-"*25)

# Se não estiver certo mostrará uma mensagem de falha
else:
    print("=-"*25)
    print("Infelizmente você errou")
    print("=-"*25)
