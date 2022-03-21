# Enunciado:
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Solução:

t = input('Digite algo: ')
print()
print('O tipo primitivo é {}'.format(type(t)))
print('Só tem espaços? {}'.format(t.isspace()))
print('É um número? {}'.format(t.isnumeric()))
print('É alfabeto? {}'.format(t.isalpha()))
print('É maisúscula? {}'.format(t.isupper()))
print('É minúscula? {}'.format(t.islower()))
print('A primeira letra é maiúscula? {}'.format(t.istitle()))
