# Enunciado:
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Solução:

a=int(input('Digite a altura em metros: '))
l=int(input('Digite a largura em metros: '))
# Já que cada lata de tinta pinta 2 metros quadrados, basta dividir o tamanho da parede(em metros quadrados) por 2. 
r=((a*l)/2)

print(f'Você precisará de {r} latas de tinta')
