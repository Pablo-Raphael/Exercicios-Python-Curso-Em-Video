# Enunciado:

"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

# Solução:

divisoes = 0

num = int(input('Quer varificar qual número? - '))

# Para cada número num de 1 até o número desejado pelo usuário
for n in range(1, num+1):
    # Verifca se o número desejado é divisível pelo número atual do laço 'for'
    if num % n == 0:
        # Se for divisível mostra na tela e adiciona à variável de divisões
        print(n)
        divisoes += 1

print("-"*50)

print(f"{num} é divisível por {divisoes} números")

# Um número primo só pode ter 2 divisões
if divisoes > 2:
    print("Logo NÃO é primo")
else:
    print("Logo É um primo")

print("-"*50)