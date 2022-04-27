# Enunciado:

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Solução:


# Recebe o número e faz ele ter 4 dígitos
num = input('escreva o número ').zfill(4)

# Mostra cada casa decimal, caso exista, se não, mostra 0
print(f'O milhar é {num[0]}')
print(f'A centena é {num[1]}')
print(f'A dezena é {num[2]}')
print(f'A unidade é {num[3]}')