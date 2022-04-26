# Enunciado:

"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

# Solução:


nome = input("Qual seu nome? ")

# .upper() transforma todas as letras da string em maiusculas
print(f"Seu nome em maiúsculo é {nome.upper()}")

# .lower() transforma todas as letras da string em minúsculas
print(f"Seu nome em minúsculo é {nome.lower()}")

# len(x) mostra quantidade de letras da string
# .count(x) mostra qual a quantidade de x valores na string
# Então o total de letras sem espaços é a soma de todas as letras menos a conta de espaços
print(f"Ele tem {len(nome) - nome.count(' ')} letras")

# .split() separa por espaços a string e a põe numa lista as divisões.
primeiroNome  = nome.split()
# Mostra a contagem de letras da primeira divisão
print(f"O primeiro nome tem {len(primeiroNome[0])} letras")