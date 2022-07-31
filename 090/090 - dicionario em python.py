# Enunciado:

"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

# Solução:


dicionario = {
    'Nome': input('Digite o nome do aluno : '),
    'Media': float(input(f'Digite a média do aluno : ')),
}

dicionario['Situação'] = 'Aprovado' if dicionario['Media'] >= 7 else 'Reprovado'

print('-'*50)

for chave, valor in dicionario.items():
    print(f'- {chave} é {valor}')
    
print('-'*50)