# Enunciado:
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# Solução:
valor=float(input('Quantos reais você tem; '))
dol=float(input('Digite a cotação do dólar; '))
result=(valor/dol)

print(f'com {valor} reais você pode comprar {result:.2f} dólares')
