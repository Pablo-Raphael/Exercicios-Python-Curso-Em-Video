# Enunciado:

"""
 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre:
 
 a média de idade do grupo,
 qual é o nome do homem mais velho e
 quantas mulheres têm menos de 20 anos.
"""

# Solução:

nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
media = 0
mulheres_menores = 0

for pessoa in range(1, 5):
    print("=-"*25)
    nome = input(f"Qual o nome da {pessoa}a pessoa? - ")
    idade = int(input('Qual a idade? - '))
    sexo = input('Qual o sexo? [M / F] - ').strip().upper()[0]

    # Independentemente de condições, a idade da pessoa deve ser incrementada à média
    media += idade

    # Se a pessoa da vez for homem e ainda não houver homem mais velho definido\
    # O homem mais velho será o da vez.
    if sexo == "M" and idade_homem_mais_velho == 0:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Se for homem e for mais velho que o homem mais velho já definido\
    # O homem mais velho será o da vez.
    elif sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Se for mulher menor de 20 anos a variável 'mulheres_menores' será atualizada.
    if sexo == "F" and idade < 20:
        mulheres_menores += 1

print("=-"*25)
print(f"A média de idade é de {media/4} anos")
print(f"O homem mais velho é o {nome_homem_mais_velho} com {idade_homem_mais_velho} anos")
print(f"E ao todo são {mulheres_menores} mulheres com menos de 20 anos")
print("=-"*25)