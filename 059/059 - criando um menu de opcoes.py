# Enunciado:

"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

# Solução:

menu = '''
[1] SOMAR
[2] MULTIPLICAR
[3] ACHAR MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
'''

num1 = int(input('Digite o PRIMEIRO número: '))
num2 = int(input('Digite o SEGUNDO número: '))
acabou = False

while not acabou:
    print("=-"*25)
    # Mostra as opções do menu
    print(menu)

    # Coleta a escolha do usuário
    op = int(input("Qual operação você escolhe? : "))
    print()

    # Soma
    if op == 1:
        print(f"A soma entre {num1} e {num2} é {num1+num2}")

    # Multiplicação
    elif op == 2:
        print(f"A multiplicação de {num1} por {num2} é {num1*num2}")

    # Maior número
    elif op == 3:
        if num1 > num2:
            print(f"O maior é o {num1}")
        elif num1 < num2:
            print(f"O maior é o {num2}")

    # Novos números
    elif op == 4:
        print("OK, REINICIANDO...\n")
        num1 = int(input('Digite o PRIMEIRO número: '))
        num2 = int(input('Digite o SEGUNDO número: '))

    # Encerrar programa
    elif op == 5:
        print("OBRIGADO POR USAR, ENCERRANDO...\n")
        acabou = True

    # Escolha inválida
    else:
        print("Opção inválida, reiniciando...")
        
print("=-"*25)