# Enunciado:

"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

# Solução:


valor1 = float(input("Digite o primeiro valor - "))
valor2 = float(input("Digite o segundo valor - "))

# Calculando a média 
media = (valor1 + valor2) / 2

# Se a média for 4.9 ou menos
if media < 5:
    print('Você foi REPROVADO !!!')

# Se a média enstiver entre 5 e 6.9
elif 5 <= media < 7:
    print('Você está em RECUPERAÇÃO !!!')

# Se for maior ou igual a 7
elif media >= 7:
    print('Você foi APROVADO !!!')