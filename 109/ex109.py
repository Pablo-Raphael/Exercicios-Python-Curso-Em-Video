def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


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