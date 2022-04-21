# Enunciado:
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Solução:

 
# importando a função que calcula a hispotenusa da biblioteca matemática
from math import hypot

# Recebendo os lados, para usá-lo na fómula da função
oposto = float(input('Digite o cateto oposto(vertical) = '))
adja = float(input('Agora digite o cateto adjacente(horizontal) = '))

# Calculando
hipo = hypot(oposto, adja)

print(f'A hipotenusa deste triangulo retângulo é de {hipo:.2f}')