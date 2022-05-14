# Enunciado:

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Solução:


num = int(input('digite o número - '))

# O sinal de % significa 'resto de divisão'.
# Não haverá resto após a divisão de um número par por 2.
# Já caso seja ímpar sobrará 1.
div = num % 2

# Se não houve resto
if div == 0:
    print("=-"*25)
    print(f"O número {num} é PAR")
    print("=-"*25)

# Se sobrou algo aós dividir o número por 2
else:
    print("=-"*25)
    print(f"O número {num} é ÍMPAR")
    print("=-"*25)