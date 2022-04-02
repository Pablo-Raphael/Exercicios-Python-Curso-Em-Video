# Enunciado:
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Solução:


n=float(input('Digite o valor do produto: '))

# Cálculo para obter 5% do número inserido
percent=(n/100*5)

# O resultado é o valor menos a porcentagem
result = (n-percent)

print(f'R${n} com 5% de desconto é {result}')
