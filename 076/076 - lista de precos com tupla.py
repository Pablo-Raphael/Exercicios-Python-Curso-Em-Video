# Enunciado:

"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

# Solução:


print('Lista de preços e produtos')

tupla = (
    'caderno', 15.50,
    'lápis', 1.75,
    'borracha', 2.00,
    'canetas', 22.30,
    'livro', 34.90,
    'mochila', 120.32,
)

# Para cada item na tupla
for pos in range(0, len(tupla)):
    
    # Se for um item em posição par significa que ele é o nome do produto
    if pos % 2 == 0:
        # O nome ocupará 30 espaços e ficará alinhado à esquerda.
        # Porém os espaços não preenchidos serão ocupados por '.'
        print(f'{tupla[pos]:.<30}', end='')

    # Se for um item em posição ímpar significa que ele é o preço do produto
    else:
        # O preço ocupará o espaços e ficará alinhado à direita. Ele também só possuirá 2 casa decimais.
        # Ou seja, 2.33333 ficaria 2.33 
        print(f'R${tupla[pos]:>8.2f}')

print('-'*40)