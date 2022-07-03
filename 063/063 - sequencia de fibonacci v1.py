# Enunciado:

"""
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""

# Solução:

anterior = 1
atual = 1
limite = 0

num = int(input('Quantos números de fibonacci mostrar? - '))

print('-' * 80)

while limite != num:
    limite += 1
    
    if num != limite:
        print(atual, end=' - ')
    else:
        print(atual)
        
    anterior = atual - anterior
    atual += anterior
   

print('-' * 80)