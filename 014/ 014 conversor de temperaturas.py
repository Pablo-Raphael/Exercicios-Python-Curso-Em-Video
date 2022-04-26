# Enunciado:
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# Solução:

# O valor é recebido e convertido para decimal
c = float(input('Digite a temperatura em graus Celsius - '))

# Para converter celsius para, multiplica-se o valor em Celsius por 1.8 e depois o soma a 32
f = c * 1.8 + 32

# Mostra o resultado na tela com precisão decimal de uma casa
print('A temperatura {:.1f} em graus fahrenheit é {:.1f}'.format(c, f))
