# Enunciado:

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Solução:


a = int(input('Digite o valor 1 - '))
b = int(input('Digite o valor 2 - '))
c = int(input('Digite o valor 3 - '))

# Verificando o maior
maior = 0
if a > b and a > c:
    maior = a
elif b > a and b > c: 
    maior = b
elif c > b and c > a:
    maior = c

# verificando o menor
menor = 0
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

# Mostrando resultados
print('-'*30)
print(f"O maior é o {maior}")
print(f"O menor é o {menor}")
print('-'*30)

# Segunda solução possível
num = [a, b, c]
print(f"O maior é o {max(num)}")
print(f"O menor é o {min(num)}")
print('-'*30)