# Enunciado:

"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""

# Solução:


num = int(input('Digite o número desejado para achar o fatorial - '))

fatorial = num

# Mostra o número do qual será feito o fatorial e faz com que o próximo print aconteça na mesma linha
print(f"{num} = ", end='')

# O laço deve parar quando chegar em 1
while num != 1:
    # Mostra os números decrescentes do fatorial na mesma linha
    print(f"{num}", end=" x ")

    # Decresce o próximo fator da multiplicação
    num -= 1

    # Multiplica o fatorial pelo fator atual
    fatorial *= num

# Fecha mostrando o resultado total
print(f"1 = {fatorial}")