# Enunciado:

"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

# Solução:


from datetime import date

# Armazenando o ano atual
ano_atual = date.today().year

nascimento = int(input('Em que ano você nasceu? - '))

idade = ano_atual - nascimento

print(f"Se você nasceu em {nascimento} você hoje tem {idade} anos")

if idade > 18:
    ano_alistamento = ano_atual - (idade - 18)
    print(f"Você deveria ter se alistado há {idade - 18} anos (Em {ano_alistamento})")

elif idade < 18:
    ano_alistamento = ano_atual + (18 - idade)
    print(f"Você ainda deverá se alistar daqui a {18 - idade} anos (Em {ano_alistamento})")

else:
    print(f"Você se alistará neste ano de {ano_atual}, corre!!!")