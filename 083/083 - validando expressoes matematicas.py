# Enunciado:

"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

# Solução:

expressao = input('Digite a expressão : ')

abrindo = fechando = 0

for letra in expressao:
    if letra == '(':
        abrindo += 1

    elif letra == ')':
        fechando += 1
    
    # A partir do momento houver mais parênteses fechando que abrindo, se configura um erro na operação.
    if fechando > abrindo:
        print('Operação inválida')
        break

if abrindo == fechando:
    print('Operação válida')
else:
    print('Operação inválida')