# Enunciado:

"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""

# Solução:


print('='*40)
print('NOTAS DO ENEM')
print('='*40)

lista = []


while True:
    aluno = []
    nome = input('Digite o nome do aluno (ou parar): ')

    if nome == 'parar': break

    aluno.append(nome)

    nota1 = float(input(f'Digite a PRIMEIRA Nota de {nome} : '))
    nota2 = float(input(f'Digite a SEGUNDA Nota de {nome} : '))
    aluno.append([nota1, nota2])
    lista.append(aluno[:])

    print('-'*40)

print('='*40)

# Mostra a nota de todos os alunos
print('{:<5}{:<15}{:<5}'.format('No.', 'Nome', 'Média'))
for posi, aluno in enumerate(lista):
    media = lista[posi][1][0] + lista[posi][1][1] / 2
    nome = lista[posi][0]
    print(f'{posi:<5}{nome:<15}{media:<5}')

print('='*40)

# Mostra as notas de um aluno específico
while True:
    nota = input('Mostrar a nota de qual aluno? (No.) : ')

    if nota == 'parar': break

    print(f'As notas de {lista[int(nota)][0]} foram {lista[int(nota)][1]}')

    print('-' * 40)