# Enunciado:

"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

# Solução:

num = int(input('Tabuada de qual número? - '))

for n in range(0, 11):
    print(f"{num} x {n} = {num * n}")