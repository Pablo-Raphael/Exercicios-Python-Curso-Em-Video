# Enunciado:

# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.\
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Solução:


import random

n1 = input('Escreva o primeiro nome: ')
n2 = input('Escreva o segundo nome: ')
n3 = input('Escreva o terceiro nome: ')
n4 = input('Escreva o quarto nome: ')

lista = [n1, n2, n3, n4]

# Embaralha a lista
random.shuffle(lista)

print(f'A ordem escolhida foi {lista}')