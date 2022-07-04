# Enunciado:

"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

# Solução:

parar = False
soma = 0
quantidade = 0

print('Soma de infinitos números')
print('Digite 999 para parar')

# Enquanto o usuário não der ordem de parada
while not parar:
    num = int(input('Digite um valor: '))

    if num != 999:
        # Incrementa a soma com o número digitado
        soma += num
        quantidade += 1
    else:
        # Ordem de parada 
        parar = True

print(f'Você digitou {quantidade} números, o resultado da soma é {soma}')