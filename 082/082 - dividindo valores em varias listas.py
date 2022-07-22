# Enunciado:

"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

# Solução:


print('='*40)
print('Digite 0 para encerrar o programa')
print('='*40)

lista = []
par = []
impar = []

while True:
    num = int(input('Digite um número : '))
    if num == 0:
        break

    lista.append(num)


print('='*40)
for numero in lista:
    # Se for par ou se for 0
    if numero % 2 == 0 or numero == 0:
        par.append(numero)
        
    else:
        impar.append(numero)

print(f'Lista inteira : {lista}')
print(f'Números pares : {par}')
print(f'Números ímpares : {impar}')
print('='*40)