# Enunciado:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Solução:

# Importando as funções necessárias para o cálculo
from math import sin, cos, tan, radians

# Recebendo o valor
area = float(input('Digite o ângulo: '))

print(f'O seno de {area} é {sin(radians(area)):.2f}')
print(f'O cosseno de {area} é {cos(radians(area)):.2f}')
print(f'O tangente de {area} é {tan(radians(area)):.2f}')