# Enunciado:

"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

# Solução:

print('='*50)

dicio = {'nome': input('Digite o nome do jogador : ')}
calculo = int(input(f'Quantas partidas {dicio["nome"]} jogou? : '))

gols = []
for c in range(1, calculo+1):
    gols.append(int(input(f'  Quantos gols {dicio["nome"]} fez na {c} partida? ')))

dicio['gols'] = gols[:]
dicio['total'] = sum(gols)

print('-'*50)
for chave, valor in dicio.items():
    print(f'A chave {chave} tem o valor {valor}')
print('-'*50)

print(f'{dicio["nome"]} jogou {len(dicio["gols"])} partidas')

for partida, gol in enumerate(gols):
    print(f'Na partida {partida+1}, fez {gol} gols')

print('='*50)