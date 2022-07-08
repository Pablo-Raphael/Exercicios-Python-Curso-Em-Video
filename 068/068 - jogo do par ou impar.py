# Enunciado:

"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

# Solução:


# Biblioteca usada para sortear a jogada do computador
from random import randint

# Título do programa
print("=" * 50)
print("Par ou impar")
print("=" * 50)

# Variável que guarda quantas vezes o usuário acertou
acertos = 0

while True:
    jogador = int(input('Escolha um número: '))

    # Escolha do computador
    computador = randint(0, 10)
    
    total = jogador + computador

    # Guarda se o usuário escolheu para ou ímpar
    escolha = ' '

    # Guarda um booleano que diz se o núemro é par ou não
    par = total % 2 == 0

    # Caso o usuário tenha colocador algo diferente de Par ou Ímpar
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar [P / I] - ')[0].upper()
    
    # Resultado
    print(f'Você: {jogador} / PC: {computador} / resultado = {total}', end=' - ')

    # Se for par...
    if par:
        # E o usuário tiver escolhido par
        if escolha == 'P':
            print('Ganhou')
            acertos += 1

        # E o usuário tiver escolhido Ímpar
        else:
            print('Perdeu')
            break

    # Se for Ímpar
    else:
        # E o usuário tiver escolhido par
        if escolha == 'P':
            print('Perdeu')
            break

        # E o usuário tiver escolhido Ímpar
        else:
            print('Ganhou')
            acertos += 1

    print("-" * 50)

print(f'Você acertou {acertos} vezes')