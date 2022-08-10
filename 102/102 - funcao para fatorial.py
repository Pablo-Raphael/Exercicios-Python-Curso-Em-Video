# Enunciado:

"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

# Solução:


def fatorial(num, mostrar=False):
    """
    - parêmetro num: Diz qual número deve ser usado para calcular o fatorial.
    - parâmetro mostrar: True = mostra a conta do fatorial / False = oculta a conta.
    - return: o fatorial de um número.
    """

    f = 1

    for num in range(num, 0, -1):
        # Se o parâmetro 'mostrar' indicar que a conta deve ser mostrada
        if mostrar:
            print(num, end= '')

            if num > 1:
                print(f' x ', end='')

            # Se for o último número
            else:
                print(' = ', end='')

        # Faz a multiplicação pelo número anterior
        f *= num
    
    print(f)
    print('=' * 50)


print('='*50)

numero = int(input('Digite o número parar o fatorial : '))
mostrar = input('Quer mostrar a conta? [S / N] : ').lower()
mostre = mostrar[0] == 's'

fatorial(numero, mostre)

help(fatorial)