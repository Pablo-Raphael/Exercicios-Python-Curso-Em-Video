# Enunciado:

# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# Solução:


# Recebe o nome, o põe em letras minúsculas e remove os espaços antes de depois
nome = input('Qual seu nome? ').lower().strip()

# Mostra True se possui e False se não possui 'silva' no nome recebido
print("=-"*25)
print(f"Seu nome tem silva? {'silva' in nome}")
print("=-"*25)