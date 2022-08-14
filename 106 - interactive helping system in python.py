# Enunciado:

"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
"""

# Solução:
while True:
    print(f"\033[31m {'=' * 80} \033[m")

    ordem = input("Digite o comando ou módulo (ou 'parar'): ")

    if ordem == 'parar':
        print(f"\033[31m {'=' * 80} \033[m") # Linha vermelha
        break

    help(ordem)