def dobrar(num=0, mostrar=False):
    return moeda(num*2) if mostrar else num*2


def metade(num=0, mostrar=False):
    return moeda(num/2) if mostrar else num/2


def aumentar(num=0, porcentagem=0, mostrar=False):
    resp = num + (num / 100) * porcentagem
    return moeda(resp) if mostrar else resp


def diminuir(num=0, porcentagem=0, mostrar=False):
    resp = num - (num / 100) * porcentagem
    return moeda(resp) if mostrar else resp


def resumir(num=0, aumente=0, reduza=0):
    print('-' * 35)
    print('ANALISE'.center(35))
    print('-'*35)
    print(f'O valor é \t\t\t{moeda(num)}')
    print(f'O dobro é \t\t\t{dobrar(num, True)}')
    print(f'A metade é \t\t\t{metade(num, True)}')
    print(f'{moeda(num)} + {aumente}% é \t{aumentar(num, aumente, True)}')
    print(f'{moeda(num)} - {reduza}% é \t{diminuir(num, reduza, True)}')
    print('-'*35)


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')