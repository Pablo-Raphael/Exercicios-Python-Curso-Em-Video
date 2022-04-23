# Enunciado:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.\
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# Solução:


# Importando as funções necessárias para o cálculo
import random

# Coleta o nome de 4 alunos
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')

# Põe o nome dos 4 alunos numa lista
lista = [a1, a2, a3, a4]

# Sorteia e armazena o sorteado numa variável
sorteado = random.choice(lista)

print (f'O sorteado é o {sorteado}')