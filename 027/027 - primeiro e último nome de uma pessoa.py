# Enunciado:

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Solução:


# Recebe o nome completo de uma pessoa
# O .split() transforma o texto recebido em uma lista
nome = input('Digite seu nome completo - ').split()

# Mostra o primeiro valor(palavra) da lista
print("=-"*25)
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[-1]}")
print("=-"*25)