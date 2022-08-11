# Enunciado:

"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

# Solução:


def jogador(nome, gols):
    if nome == '':
        nome = '<Desconhecido>'

    if gols == '' or gols[0] not in '1234567890':
        gols = 0

    print('-' * 50)
    print(f'O jodador {nome} fez {gols} gols')
    print('='*50)


print('='*50)

jogador(
    input('Digite o nome do jogador : '),
    input('Quantos gols foram feitos? : ')
)