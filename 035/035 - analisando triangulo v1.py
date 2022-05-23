# Enunciado:

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Solução:


# Para que seja possível formar um triângulo é preciso que cada lado seja menor que a soma dos outros dois:
# lado a menor que b + c
# lado b menor que c + a
# lado c menor que a + b

a = float(input('Digite o lado A - '))
b = float(input('Digite o lado B - '))
c = float(input('Digite o lado C - '))

if a < b + c and b < a + c and c < b + a:
    print('Sim, é possível fazer um triângulo com essas medidas.')
else:
    print('não é possível fazer um triângulo com essas medidas')