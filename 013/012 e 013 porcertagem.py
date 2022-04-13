# Enunciado:
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Solução:

# Recebendo o valor do salário
n=float(input('Digite o valor do salário: R$'))

# Calculando valor do acráscimo porcentagem
c=(n*15/100)

# Somando o valor ao salário
r=(n+c)

print('{} com 15% de aumento é {}'.format(n,r))
