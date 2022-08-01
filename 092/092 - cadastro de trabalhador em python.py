# Enunciado:

"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

# Solução:


from datetime import date

dicio = {}

ano_atual = date.today().year

dicio['Nome'] = input('Digite o nome : ').title()
dicio['Idade'] = ano_atual - int(input('Digite o ano de nascimento : '))
dicio['Carteira'] = int(input('Digite o código da Carteira de Trabalho : '))

if dicio['Carteira'] != 0:
    dicio['Contratação'] = int(input('Digite o ano de contratação : '))
    dicio['Salário'] = float(input('Digite o salário: R$').replace(',', '.'))
    dicio['Aposentadoria'] = 70 - dicio['Idade']

print('*'*45)
# Mostra os dados com uma tabulação(espaçamento)
for chave, valor in dicio.items():
    print(f'{chave:^13} é {valor:<6}')
print('*'*45)