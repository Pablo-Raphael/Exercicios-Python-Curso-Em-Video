# Enunciado:

"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

# Solução:


print('='*50)
print('Números de 0 a 20 por extenso')
print('='*50)

# Tupla (imutável) com os números de 0 a 20 por extenso
numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
    )

extenso = int(input('Qual o número desejado? - '))

# Não passa até que o número esteja entre 0 e 20
while extenso < 0 or extenso > 20:
    extenso = int(input('Número inválido, tente novamente : '))

# Mostra a posição da tupla que corresponde ao número desejado
print(f'você escreveu o número : {numeros[extenso]}')