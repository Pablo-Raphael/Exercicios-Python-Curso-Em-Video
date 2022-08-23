def leiafloat(txt=''):
    num = input(txt).replace(',', '.').strip()
    while not num.replace('.', '').isnumeric():
        print(f'\033[31mERRO, \"{num}\" não é válido\033[m')
        num = input(txt).replace(',', '.').strip()
    return float(num)


def leiaint(txt=''):
    num = input(txt).replace(',', '.').strip()
    while not num.isnumeric():
        print(f'\033[31mERRO, \"{num}\" não é válido\033[m')
        num = input(txt)
    return int(num)