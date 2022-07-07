# Enunciado:

"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

# Solução:


while True:
    print("~"*40)
    num = int(input("Quer ver a tabuada de qual número? - "))

    # Se o número fro maior ou igual a 0
    if num >= 0:
        
        # Mostra os 10 primeiros números da tabuada
        for tabuada in range(1, 11):
            print(f'{num} x {tabuada} = {num*tabuada}')

    # Se o número for menor que 0
    else:
        print('~'*40)
        break