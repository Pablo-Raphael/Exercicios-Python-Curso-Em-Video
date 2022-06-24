# Enunciado:

"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

# Solução:


# Biblioteca que ajuda com datas
from datetime import date

# Armazena o ano atual
ano_atual = date.today().year

# Variável que armazenará o número de maiores de idade
maiores = 0

for pessoa in range(1, 8):
    # Armazena o ano de nascimento da pessoa da vez
    ano_nascimento = int(input(f"Em que ano a {pessoa}a pessoa nasceu? - "))

    # Sa idade for maior ou igual a 18 somará 1 à variável de pessoas maiores de idade
    if (ano_atual - ano_nascimento) >= 18:
        maiores += 1

print(f"{maiores} pessoas têm mais de 18 anos")