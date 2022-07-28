# Enunciado:

"""
aça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

# Solução:

from random import randint

print('='*40)
print("MEGA SENA")
print('='*40)

lista = []
auxiliar = []

quant = int(input('Quantos números sortear? : '))
print(f'Gerando {quant} números')

for jogo in range(1, quant+1):
    # Uma lista com um 6 números aleatórios, cada um entre 0 e 60
    auxiliar = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]

    lista.append(auxiliar[:])

    print(f'Jogo {jogo:0>2}: {auxiliar}')

    auxiliar.clear()

print('='*40)