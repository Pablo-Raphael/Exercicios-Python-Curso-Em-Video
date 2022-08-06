# Enunciado:

"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

# Solução:

def linha():
    print("=" * 50)


def personalizado(inicial, final, pulando):
    """ Funçao que personaliza uma contagem """

    # Se o número de pulos for zero
    if pulando == 0:
        pulando = 1

    linha()
    print(f'Ok, contando de {inicial} a {final} de {pulando} em {pulando}')

    # pulos comuns
    if final > inicial and pulando > 0:
        for numero in range(inicial, final+1, pulando):
            print(numero, end=' ')
        print('FIM')

    # pulos contrarios
    if final < inicial:
        if '-' in str(pulando):
            pulando = int(str(pulando).replace('-', ''))
            print('passou')
        for numero in range(inicial, final-1, -pulando):
            print(numero, end=' ')
        print('FIM')


# A
personalizado(1, 10, 1)

# B
personalizado(10, 0, 2)

# Customizado
linha()
print('Agora é você quem manda !!')

inicio = int(input('Começar com : '))
fim = int(input('Terminar com : '))
pulo = int(input('Pulando : '))

personalizado(inicio, fim, pulo)

linha()