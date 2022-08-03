# Enunciado:

"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

# Solução:


print('='*45)
print("'parar' para encerrar")
print('='*45)

lista = []
dicio = {}

# Cadastro na lista
while True:
    nome = input('Digite o nome : ').title()

    if nome == 'Parar':
        print('-' * 45)
        break

    dicio['nome'] = nome

    idade = int(input('Digite a idade : '))
    dicio['idade'] = idade

    sexo = input('Digite o sexo [M / F]: ')[0].upper()
    while sexo not in 'MF':
        sexo = input('M para mascuino ou F para feminino : ')[0].upper()
    dicio['sexo'] = sexo
    
    lista.append(dicio.copy())
    dicio.clear()

    print('-'*45)


# total de pessoas
print(f'1) Ao todo temos {len(lista)} pessoas cadastradas')

# idade
idade = []
for c in lista:
    idade.append(c['idade'])
print(f'2) A média de idade é {(sum(idade)/len(lista)):.1f} anos')

# mulheres
print(f'3) As mulheres são: ')
totmulheres = 0
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(f"   {pessoa['nome']} é mulher")

# pessoas acima da média
print('4) Lista das pessoas acima da média de idade: ')
media = sum(idade) / len(lista)
for pessoa in lista:
    if pessoa['idade'] > media:
        print(f'   Nome = {pessoa["nome"]} / Sexo = {pessoa["sexo"]} / Idade = {pessoa["idade"]}')


print('='*45)