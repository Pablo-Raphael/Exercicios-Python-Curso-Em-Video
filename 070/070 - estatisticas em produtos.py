# Enunciado:

"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

# Solução:

print('='*50)
print('Loja Muito Boa')
print('='*50)

total = milcima = prod_mais_barato = menor_preco = num_de_produtos = 0

while True:
    produto = input('Digite a descrição do produto: ').upper()

    if produto == 'PARAR':
        print('-' * 20, 'encerrado', '-' * 20)
        break

    preco = float(input('Digite o preço do produto: R$'))
    total += preco

    if preco > 1000:
        milcima += 1

    if num_de_produtos == 0 or preco < menor_preco:
        menor_preco = preco
        prod_mais_barato = produto

    num_de_produtos += 1

    print('-'*50)

print(f'O valor total foi de R${total}')
print(f'Tivemos {milcima} produtos acima de R$1000,0 reais')
print(f'O produto mais barato foi {prod_mais_barato} custando R${menor_preco}')