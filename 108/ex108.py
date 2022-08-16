def dobrar(num=0):
    return num*2


def metade(num=0):
    return num/2


def aumentar(num=0, porcentagem=0):
    return num + (num / 100) * porcentagem


def diminuir(num=0, porcentagem=0):
    return num - (num / 100) * porcentagem


def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')