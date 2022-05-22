# Enunciado:

"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
"""

# Solução:

sal = float(input('digite o valor do salário atual - '))

if sal <= 1250:
    # Formula para aumento percentual
    valor = sal + (sal / 100) * 15

    # O :.2f arredonda para 2 casas decimais, para que não seja mostrado um número muito longo.
    print(f"O aumento será de 15% -> {valor:.2f} reais")
else:
    valor = sal + (sal / 100) * 10
    
    print(f"O aumento será de 10% -> {valor:.2f} reais")