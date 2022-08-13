# Enunciado:

"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')
"""

# Solução:


corVermelha = "\033[31m"
corNeutra = "\033[m"

def leiaInt(num):
    while not num.isnumeric():
        print(f'{corVermelha}ERRO, DIGITE UM NÚMERO VÁLIDO{corNeutra}')
        num = input('Digite um número : ')

    print('-'*50)

    return num


print('='*50)

num = leiaInt(input('Digite um número : '))

print(f'Você digitou o número {num}')

print('='*50)