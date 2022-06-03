# Enunciado:

"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
"""

# Solução:

valor = float(input("Digite o valor do produto R$: "))

print("""
[1] Dinheiro / cheque
[2] crédito à vista
[3] 2x no cartão
[4] 3x ou + no cartão
""")

opc = int(input("Digite o número correspondente à forma de pagamento - "))

if opc == 1:
    print(f"O valor será de {valor - ((valor / 100) * 10)}")

elif opc == 2:
    print(f"O valor será de {valor - ((valor / 100) * 5)}")

elif opc == 3:
    print(f"O valor será de {valor}")

elif opc == 4:
    print(f"O valor será de {valor + ((valor / 100) * 20)}")

else:
    print("O número não corresponde à tabela")