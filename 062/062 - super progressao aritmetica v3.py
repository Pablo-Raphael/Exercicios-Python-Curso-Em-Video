# Enunciado:

"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

# Solução:

limite = 10
vezes = 0

print('='*50)

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

print('='*50)

# Enquanto não repetiu o número de vezes definido em 'limite'
while vezes < limite:
    # Diz à variável que houve mais uma repetição
    vezes += 1
    
    # Mostra o número da PA
    print(num, end=' - ' if vezes < limite else '\n')

    # Incrementa o número para mostrar na próxima repetição
    num += razao

    # Se atingiu o limite
    if vezes == limite:
        # Pergunta se o usuário que repetir
        repetir = int(input('quantas mais PAs mostrar? (0 para PARAR) - '))

        # Se não quiser o programa encerra
        if repetir == 0:
            print('Você visualizou {} PAs'.format(limite))
        # Se quiser o limite passa a ser o númeor de PAs que o usuário quer
        else:
            limite += repetir

print('='*50)