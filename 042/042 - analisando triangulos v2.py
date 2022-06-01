# Enunciado:

"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""

# Solução:

a = float(input("Digite o lado A - "))
b = float(input("Digite o lado B - "))
c = float(input("Digite o lado C - "))

triangulo = False

# Verifica se as medidas formam um triângulo
if a < b + c and b < a + c and c < b + a:
    triangulo = True

# Se for possível formar um triângulo
if triangulo:
    # Se o triângulo possuir todos os lados iguais
    if a == b == c:
        print('É possível formar um triangulo EQUILATERO')

    # Se o triângulo possuir ao menos um dos lados iguais
    elif a == b or b == c or c == a:
        print('É possível formar um triângulo ISOCELES')

    # Caso nenhum lado seja igual
    else:
        print('É possível formar um triângulo ESCALENO')

# Se não for possível formar um triângulo
else:
    print("Não é possível fazer um triângulo com essas medidas")