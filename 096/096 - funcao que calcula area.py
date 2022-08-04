# Enunciado:

"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

# Solução:


def area(larg, compri):
    area = larg * compri
    print(f'A área de um terreno {larg} x {compri} é: {area:.2f} metros quadrados')


print("="*40)
print("Calculando área")
print("="*40)

largura = float(input('Largura em METROS(m) : ').replace(',', '.'))
comprimento = float(input('Comprimento em METROS(m) : ').replace(',', '.'))

area(largura, comprimento)