# Enunciado:

"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

# Solução:


from random import randint
from operator import itemgetter

print('='*40)

dicio = {}
auxiliar = ''

for c in range(1, 5):
    dicio[f'Jogador {c}'] = randint(1, 6)

for chave, valor in dicio.items():
    print(f'{chave} tirou {valor} no dado')

# O itemgetter 1 é a ordem de valor, o 0 é a ordem de chave
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)

print('-'*40)
for posicao, pessoa in enumerate(ranking):
    print(f'{posicao+1} lugar : {pessoa[0]} com {pessoa[1]} pontos')
print('='*40)