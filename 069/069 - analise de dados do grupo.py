# Enunciado:

"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

# Solução:


mais18 = homens = mulheres20 = 0

while True:
    # Coleta a idade
    idade = int(input('Idade: '))

    # Só passa se o usuário dgitar um sexo válido
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M / F]: ')[0].strip().upper()

    # Se for maior de idade
    if idade >= 18:
        mais18 += 1

    # Númeoro de homens
    if sexo == 'M':
        homens += 1

    # Se for mulher e tiver no mínimo 20 anos
    if sexo == 'F' and idade >= 20:
        mulheres20 += 1

    # Se o usuário quiser parar
    cont = input('Quer continuar? [S / N]: ')[0].strip().upper()
    print('-' * 40)
    if cont == 'N':    
        break


print(f'Há {mais18} pessoas com mais de 18 anos')
print(f'Tem {homens} homens')
print(f'E {mulheres20} mulheres com mais de 20 anos')