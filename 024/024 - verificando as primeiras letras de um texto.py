# Enunciado:

# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

# Solução:


# Recebe o nome da cidade, retira os espaços antes e depois e o armazena em letras mińusculas.
cidade = input('Escreva o nome da cidade em que você nasceu - ').lower().strip()

# Mostra 'True' se os 5 primeiros caracteres forem a palavra 'santo' 
print(cidade[:5] == 'santo')