# Enunciado:

"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

# Solução:

# Coleta a frase e a põe em letras maiúsculas
frase = input("Digite a frase: ").upper()

sem_espacos = "".join(frase.split())

inverso = sem_espacos[::-1]

if inverso == sem_espacos:
    print('Esta acertou, é um Palindromo')
else:
    print('Você ainda não acertou o Palindromo')
