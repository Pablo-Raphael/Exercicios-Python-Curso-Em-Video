# Enunciado:

"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

# Solução:


vel = float(input("Qual a velocidade do carro? - "))

# Se a velocidade do carro for menor ou igual a 80km/h
if vel <= 80:
    print("=-"*25)
    print("Seu carro não foi multado")
    print("=-"*25)

# Se for maior que 80 o carro será multado
else:
    # Para cada Km/h acima o limite será pago 7 reais
    multa = (vel - 80) * 7
    print("=-"*25)
    print(f"Sua multa será de {multa} reais.")
    print("=-"*25)