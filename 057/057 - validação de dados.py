# Enunciado:

"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

# Solução:


# Coleta a primeira letra do sexo digidado e a põe em maiúsculo
sexo = input("Qual seu sexo? [F/M]: ").upper()[0]

# Enquanto a primeira letra não for M ou F ou caso a pessoa não tenha digitado nada
while sexo not in "MF" or sexo == "":
    sexo = input("Dados inválidos, digite novamente [F/M] : ").upper()[0]

if sexo == "M":
    print("OK, sexo MASCULINO registrado com sucesso.")

elif sexo == "F":
    print("OK, sexo FEMININO registrado com sucesso.")