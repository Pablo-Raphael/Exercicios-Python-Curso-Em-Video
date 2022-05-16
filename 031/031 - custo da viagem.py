# Enunciado:

"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

# Solução:


km = float(input('Digite a distância em KM - '))

# Se a distância for menor ou igual à 200
if km <= 200:
    preco = km * 0.50
    print(f"O preço por viajar {km}KMs é de {preco} reais")

# Se a distância passar de 200
else:
    preco = km * 0.45
    print(f"O preço por viajar {km}KMs é de {preco} reais")