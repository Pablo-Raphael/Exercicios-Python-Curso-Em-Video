# Enunciado:

"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

# Solução:
## Alta complexidade ##


print('='*45)
print("'parar' para encerrar")
print('='*45)

lista = []

while True:
    dicio = {}
    gols = []

    nome = input('Digite o nome do jogador : ').title()

    if nome == 'Parar':
        print('-' * 45)
        break

    dicio['nome'] = nome

    calculo = int(input(f'Quantas partidas {nome} jogou? : '))
    
    for partida in range(1, calculo+1):
        gols.append(int(input(f'    Quantos gols {nome} fez na {partida} partida? ')))

    # Salvando tudo
    dicio['gols'] = gols[:]
    dicio['total'] = sum(gols)
    lista.append(dicio.copy())
    print('-'*45)


# Mostra em formato de tabela os dados de todos os cadastrados
print(f'{"No.":<4}{"nome":<12}{"gols":<20}{"total":<4}')

for numero, jogador in enumerate(lista):
    print(f'{numero:<4}{jogador["nome"]:<12}{str(jogador["gols"]):<20}{jogador["total"]:<4}')

print('-'*45)

# Mostra o desempenho de um jogador em específico
while True:
    jogador = int(input('Mostrar desempenho de quem? (999 = parar) : '))
    
    if jogador == 999:
        print('=' * 45)
        break

    print(f'> Eis os dados de {lista[jogador]["nome"]}')

    gols = lista[jogador]["gols"]
    numDePartidas = len(gols)
    for partida in range(numDePartidas):
        nome = lista[jogador]["nome"]
        print(f'  No {partida+1}* jogo {nome} fez {gols[partida]} gol(s)')

    print('-'*45)