# Enunciado:

"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""

# Solução:


def studentStatistics(grades = list, showSituation = bool):
    average = sum(grades) / len(grades)

    studentData = {
        'Total': len(grades),
        'Maior nota': max(grades),
        'Menor nota': min(grades),
        'Média': round(average, 2)
        }

    # Se o usuário pediu para mostrar a situação da turma (passada a intenção por parâmetro)
    if showSituation:
        # Se a média for menor que 5
        if average < 5:
            studentData['Situação'] = 'RUIM'
        
        # Se for menor que 8
        elif average < 8:
            studentData['Situação'] = 'BOM'

        # Se for maior ou igual a 8
        else:
            studentData['Situação'] = 'PERFEITO'

    return studentData


print('='*45)

# Põe as notas do aluno numa lista
list = []
student = 1
while True:
    grade = float(input(f'Digite uma nota para o aluno {student} (999 encerra) : '))

    # Para o loop caso o usuário digite 999
    if grade == 999:
        break
    
    student += 1
    list.append(grade)

showSituation = input('Mostrar a situação da turma? [S / N] : ')[0].upper() == "S"

print('-'*45)

# Chama e armazena o retorno da função
data = studentStatistics(list, showSituation)

# Mostra os dados do dicionário
for chave, valor in data.items():
    print(f'{chave:^20} > {valor}')

print('='*45)