# Enunciado:

"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

# Solução:


# Biblioteca com as funções
from socket import gethostbyname, create_connection


def conectadointernet():
    servidorRemoto = 'www.google.com.br'
    
    try:
        host = gethostbyname(servidorRemoto)
        create_connection((host, 80), 2)
        
    except:
        print('não acessível')

    else:
        print('sim, está acessível')


conectadointernet()