# Enunciado:

"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
 retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

# Solução:


from datetime import date

def voto(nascimento):
    anoAtual = date.today().year
    idade = anoAtual - nascimento

    print(f'Com {idade} anos seu voto: ', end='')

    if idade > 60:
        return 'NÃO É OBRIGATÓRIO'

    elif idade >= 18:
        return 'É OBRIGATÓRIO'

    elif idade < 18:
        return 'NÃO É PERMITIDO'

    print('=' * 50)


print('='*50)
nasc = int(input('Digite seu ano de nascimento : '))
print(voto(nasc))