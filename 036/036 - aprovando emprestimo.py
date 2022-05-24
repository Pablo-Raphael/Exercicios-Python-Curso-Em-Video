# Enunciado:

"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

# Solução:

val = float(input('Digite o valor total da CASA - R$'))
sal = float(input('Digite o valor do SALÁRIO - R$'))
ano = int(input('Em quantos anos você quer pagar? - '))

# Cálculo para o valor da parcela
parcela = val / (ano * 12)

# Cálculo para obter 30% do salário
trintaSalario = sal / 100 * 30

print(f"A parcela ficará no valor de {parcela:.2f} reais")

# Se a parcela for menor ou igual a 30% do salário
if parcela <= trintaSalario:
    print("E seu emprestimo SERÁ aprovado")

else:
    print("E seu empréstimo NÃO será aprovado")