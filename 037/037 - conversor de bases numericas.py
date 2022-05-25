# Enunciado:

"""
Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal.
"""

# Solução:

# Número a ser convertido
num = int(input('Digite o valor INTEIRO - '))

# Recebendo para qual base o número será convertido
print("""
[1] Binário
[2] Hexadecimal
[3] Octal
""")
op = int(input("Escolha uma das bases - "))

# Mostrando de acordo com a opção
print("-"*50)
if op == 1:
    print(bin(num)[2:])
elif op == 2:
    print(hex(num)[2:])
elif op == 3:
    print(oct(num)[2:])
else:
    print('O valor selecionado se encontra dentre as opções')
print("-"*50)