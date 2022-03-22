# Enunciado:
# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

# Solução:
n = int(input('digite um número '))
ant = (n-1)
suc = (n+1)
print('o antecessor de {} é {} e seu sucessor é {}'.format(n, ant, suc))
