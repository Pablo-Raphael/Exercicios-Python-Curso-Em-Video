# Enunciado:

"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5:	Abaixo do Peso
– Entre 18,5 e 25:		Peso Ideal
– 25 até 30:			Sobrepeso
– 30 até 40:			Obesidade
– Acima de 40:			Obesidade Mórbida
"""

# Solução:

peso = float(input("Qual seu peso em KG? - "))
altura = float(input("Qual sua altura em METROS? - "))

# Peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:	print("Abaixo do Peso")
elif imc < 25:	print("Peso Ideal")
elif imc < 30:	print("Sobrepeso")
elif imc < 40:	print("Obesidade")
else:			print("Obesidade Mórbida")