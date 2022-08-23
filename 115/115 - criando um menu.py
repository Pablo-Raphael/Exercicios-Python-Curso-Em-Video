# Enunciado:

"""
Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
"""

# Solução:

from utilidades import *
from ex115 import *

# O arquivo de texto que guarda os dados se chama 'database.txt'
arquivo = '115/database.txt'
# Se ele não existe, será criado
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    menuPrincipal()

    opcao = leiaint('Sua escolha : ')

    while opcao not in (1, 2, 3):
        opcao = leiaint('Sua escolha (ENTRE 1 E 3) : ')

    if opcao == 1:
        cabecalho('OPÇÃO 1 - VER CADASTRADOS')
        lerArquivo(arquivo)

    elif opcao == 2:
        cabecalho('OPÇÃO 2 - CADASTRAR PESSOAS')
        nome = input('Nome : ')
        idade = leiaint('Idade : ')
        cadastrar(arquivo, nome, idade)

    elif opcao == 3:
        cabecalho('SAINDO AGORA, ATÉ MAIS')
        break