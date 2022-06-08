# Enunciado:

"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

# Solução:


# biblioteca de tempo
from time import sleep

# Para cada segundo num intervalo de 10 a 0 (subtraindo um a cada segundo)
for segundo in range(10, 0, -1):
    # Segundo atual
    print(segundo)

    # Esperando um segundo para a próxima vez
    sleep(1)
    
# Fim do programa. Fogos estourando
print('Estourando fogos, kabum !!!')