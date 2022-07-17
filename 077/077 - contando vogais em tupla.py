# Enunciado:

"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

# Solução:


tupla = (
'aprender',
'programar',
'linguagem',
'python',
'curso',
'gratis',
'estudar',
'praticar',
'trabalhar',
'mercado',
'programador',
'futuro',
)

print('-'*50)

for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')

    for letra in palavra:
        # Se a letra atual for uma vogal, a mostrará
        if letra in 'aeiou':
            print(letra.upper(), end=' ')
    
print()
print('-'*50)