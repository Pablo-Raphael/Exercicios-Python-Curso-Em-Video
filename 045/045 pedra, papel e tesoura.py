# Enunciado:

"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

# Solução:

from random import randint

print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")
jogador = int(input("Escolha a sua jogada: "))

# Jogada aleatória do computador
computador = randint(1, 3)

if computador == 1:   print('\nO computador escolheu PEDRA')
elif computador == 2: print('\nO computador escolheu PAPEL')
elif computador == 3: print('\nO computador escolheu TESOURA')

# Se o jogador escolher a mesma coisa que o usuário escolheu
if jogador == computador: print('O resultado foi EMPATE')

# Se o jogador escolheu PEDRA e o computador escolheu PAPEL
elif jogador == 1 and computador == 2: print('O resultado foi DERROTA')
# Se o jogador escolheu PEDRA e o computador escolheu TESOURA
elif jogador == 1 and computador == 3: print('O resultado foi VITÓRIA')

# Se o jogador escolheu PAPEL e o computador escolheu PEDRA
elif jogador == 2 and computador == 1: print('O resultado foi VITÓRIA')
# Se o jogador escolheu PAPEL e o computador escolheu TESOURA
elif jogador == 2 and computador == 3: print('O resultado foi DERROTA')

# Se o jogador escolheu TESOURA e o computador escolheu PEDRA
elif jogador == 3 and computador == 1: print('O resultado foi DERROTA')
# Se o jogador escolheu TESOURA e o computador escolheu PAPEL
elif jogador == 3 and computador == 2: print('O resultado foi VITÓRIA')

else: print('Ocorreu um erro !!!')