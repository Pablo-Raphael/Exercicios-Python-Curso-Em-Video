# Enunciado:

"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

# Solução:


from random import randint

# O computador armazena um número aleatório entre 0 e 10
computador = randint(0, 10)

print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")

# Variáveis usadas par guardar as informações do jogo
acertou = False
tentativas = 0

# Enquanto o usuário não acertou
while not acertou:
    jogador = int(input("Qual é seu palpite? - "))
    tentativas += 1

    # Se o palpite do usuário foi o correto, a variável que controla o while será marcada como True
    if jogador == computador:
        acertou = True

    else:
        # Se o palpite for maior que a escola do computador
        if jogador > computador:
            print("Menos... tente novamente")

        # Se o palpite for menor que a escola do computador
        elif jogador < computador:
            print("Mais... tente novamente")

print(f"Acertou com {tentativas}. Parabéns")