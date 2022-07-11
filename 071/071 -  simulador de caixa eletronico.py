# Enunciado:

"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

# Solução:


print('='*50)
print('Banco do Python')
print('='*50)

quant = cinquenta = vinte = dez = um = 0

num = int(input('Digite o valor que você quer sacar: '))

while quant < num:
    # Põe mais uma nota de 50 caso depois de somado não ultrapasse o valor do saque
    if quant + 50 <= num:
        quant += 50
        cinquenta += 1

    # Põe mais uma nota de 20 caso depois de somado não ultrapasse o valor do saque
    elif quant + 20 <= num:
        quant += 20
        vinte += 1

    # Põe mais uma nota de 10 caso depois de somado não ultrapasse o valor do saque
    elif quant + 10 <= num:
        quant += 10
        dez += 1

    # Põe mais uma nota de 0 caso depois de somado não ultrapasse o valor do saque
    elif quant + 1 <= num:
        quant += 1
        um += 1

print()

print(f'{cinquenta} notas de R$50,00')
print(f'{vinte} notas de R$20,00')
print(f'{dez} notas de R$10,00')
print(f'{um} notas de R$1,00')