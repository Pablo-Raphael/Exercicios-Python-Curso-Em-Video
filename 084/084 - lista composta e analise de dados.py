# Enunciado:

"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

# Solução:

#Todas as listas globais
dados = []
pessoas = []
peso_total = []
pessoas_maior_peso = []
pessoas_menor_peso  = []


#Dados inseridos pelo usuário
while True: 
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    dados.clear()

    proximo = input('Quer continuar? (S/N):')[0].upper()
    if proximo == 'N':
        break

# Separando todos os pesos na lista > peso_total
for peso in pessoas:
    peso_total.append(peso[1])

# Checando o peso máximo e mínimo 
maior_peso = max(peso_total)
menor_peso = min(peso_total)

# Identificando os respectivos nomes de peso Max/Min
for pes in pessoas:
    if pes[1] == maior_peso:
        pessoas_maior_peso.append(pes[0]) 
    if pes[1] == menor_peso:
       pessoas_menor_peso.append(pes[0]) 

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {pessoas_maior_peso}')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {pessoas_menor_peso}')