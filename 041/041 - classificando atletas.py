# Enunciado:

"""
 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

# Solução:


from datetime import date

ano_nascimento = int(input('Digite o ano em que você nasceu - '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Até 9 anos
if idade <= 9:
    print('Você é um atleta MIRIM')

# Até 14 anos
elif idade <= 14:
    print('Você é um atleta INFANTIL')

# Até 19 anos
elif idade <= 19:
    print('Você é um atleta JUNIOR !!!')

# Até 25 anos
elif idade <= 25:
    print('Você é um tleta SÊNIOR !!!')

# Mais de 25 anos
else:
    print('Você é um atleta MASTER !!!')