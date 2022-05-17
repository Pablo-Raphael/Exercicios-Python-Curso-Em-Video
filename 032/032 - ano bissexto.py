# Enunciado:

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Solução:


"""
Para um ano ser bissexto ele precisa cumprir ao menos um dos seguintes requisitos:
* Divisível por 4 mas não divisível por 100.
* Divisível por 400.  
"""

# bibliotceca que ajuda a capturar a data de hoje
from datetime import date

# Recebe o ano desejado e transforma num tipo inteiro
ano = int(input('Digite o ano que deseja ou 0 para escolher o ano atual - '))

# Se o usuário escolheu o ano atual
if ano == 0:
    # A variável 'ano' passará a guardar o ano atual
    ano = date.today().year

# Se o ano cumprir um ou outro requisito para ser um ano bissexto (descritos no início)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")

# Se não cumprir nenhum requisito
else:
    print(f"O ano {ano} não é bissexto")


"""
Exlicando as condições do bloco if:

if                  se
ano % 4 == 0        o resto da divisão do ano por 4 for 0 (divisível por 4)
and                 ao mesmo tempo que
ano % 100 != 0      o resto da divisão do ano por 100 seja diferente de 0 (não divisível por 100)
or                  ou se
ano % 400 == 0      o resto da divisão do ano por 400 for 0 (divisível por 400)
:                   então
"""
