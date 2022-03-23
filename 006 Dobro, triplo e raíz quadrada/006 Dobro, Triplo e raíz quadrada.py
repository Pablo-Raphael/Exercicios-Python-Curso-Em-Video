# Enunciado:
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Solução:

n=int(input('Escreva o número desejado: '))
dobro=(n*2)
triplo=(n*3)
raiz=(n**(1/2))
print('O número {} tem como dobro {} ,{} como triplo e {:.3f} como raiz quadrada'.format(n,dobro,triplo,raiz))
