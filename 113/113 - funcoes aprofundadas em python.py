# Enunciado:

"""
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

# Solução:


def leiaint(txt):
    while True:
        # Tenta
        try:
            num = int(input(txt))

        # Se houver um erro do tipo TypeError ou ValueError
        except (TypeError, ValueError):
            print('Erro, número inválido')
            # O continue faz com que o programa passepara o próximo laço do loop instantaneamente.
            continue

        # Se não houve erro
        else:
            return num


def leiafloat(txt):
    while True:
        try:
            num = float(input(txt).replace(',', '.'))
        except (TypeError, ValueError):
            print('Erro, número inválido')
        else:
            return num


inteiro = leiaint('Digite um número inteiro : ')
decimal = leiafloat('Digte um número decimal : ')
print(f'O número inteiro é {inteiro} e o decimal é {decimal}')