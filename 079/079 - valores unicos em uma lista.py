# Enunciado:

"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

# Solução:


print('-'*40)
print('Números únicos')
print('Digite 0 para encerrar')
print('-'*40)

lista = list()

while True:
    num = int(input('Digite um número : '))

    if num == 0:
        break

    if num not in lista:
        lista.append(num)
        print('Adicionado com SUCESSO')
    
    else:
        print('Número já adicionado anteriormente')

    print('-'*40)

lista.sort()
print(f'Os números digitados foram : {lista}')

print('-'*40)