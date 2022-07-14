# Enunciado:

"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

# Solução:


times = (
    'Internacional', 'São Paulo', 'Flamengo', 'Atlético-MG', 'Palmeiras', 'Grêmio', 'Fluminense', 'Corinthians', 'Santos',
    'Ceará SC', 'Bragantino', 'Athletico-PR', 'Atlético-GO', 'Fortaleza', 'Bahia', 'Sport Recife', 'Vasco da Gama', 'Coritiba', 'Goiás', 'Botafogo',
)

print('='*100)
# Mostra os times de 0 a 5 (o último index é ignorado, então é de 0 a 4)
print(f'Os 5 primeiros são : {times[0:5]}')
print('='*100)
# O sinal de menos é uma inversão, ou seja, 2 mostra o segundo, -2 mostra o penúltimo 
print(f'Os 4 últimos são {times[-4:]}')
print('='*100)
# Sorted organiza em ordem
print(f'Os times em ordem alfabética : {sorted(times)}')
print('='*100)
# .index() encontra a posição de algo
print(f'O Bragantino está na {times.index("Bragantino")+1}* posição')
print('='*100)