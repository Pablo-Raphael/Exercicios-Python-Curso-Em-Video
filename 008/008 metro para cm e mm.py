# Enunciado:
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Solução:


# Recebe do usuário o valor em metros.
m=int(input('digite o valor em METROS; '))

# Para converter M para Cm basta multiplicar por 100:
cm=(m*100)

# Já para converter de M para mm basta multiplicar por 1000:
mm=(m*1000)

print(f'{m}MTs tem {cm}cm e {mm}mm')
