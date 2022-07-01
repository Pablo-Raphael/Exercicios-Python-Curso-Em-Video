# Enunciado:

"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

# Solução:


vezes = 1

print('='*50)

num = int(input('Digite o primeiro termo: '))

razao = int(input('Digite a razão da PA: '))

while vezes <= 10:
    print(num, end=' - ' if vezes < 10 else'\n')
    num += razao
    vezes += 1
    
print('='*50)