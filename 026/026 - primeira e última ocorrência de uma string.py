# Enunciado:

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Solução:

texto = input('Digite a frase para análise - ')

print(f"A letra 'a' aparece {texto.count('a')} vezes")
print(f"A ÚLTIMA letra 'A' aparece na posição {texto.rfind('a')}")
print(f"A PRIMEIRA letra 'A' aparece na posição {texto.find('a')}")