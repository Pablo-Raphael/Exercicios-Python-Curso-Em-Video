def linha():
    print('-'*40)


def cabecalho(txt):
    linha()
    print(str(txt).center(40))
    linha()


def menuPrincipal():
    cabecalho('MENU PRINCIPAL')
    print('\033[033m1 - \033[34mVer pessoas cadastradas\033[m')
    print('\033[033m2 - \033[34mCadastrar pessoas\033[m')
    print('\033[033m3 - \033[34mEncerrar sistema\033[m')
    linha()

# Verifica se X arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Cria o arquvo que guarda os dados
def criarArquivo(nome):
    try:
        # Vai abrir e/ou criar e logo em seguida fechar, já que o intuito é só criar
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Problema ao criar arquivo')
    else:
        print(f'Arquivo {nome} criado')

# Lê e mostra todos os dados no arquivo
def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('erro')
    else:
        for linha in arquivo:
            # Remove a quebra de linha e separa por ';'
            dados = linha.replace('\n', '').split(';')
            print(f'{dados[0]:<30} {dados[1]:>3} anos')

# Cadastra uma nova pessoa no arquivo
def cadastrar(arq, nome='Não informado', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Não foi possível cadatrar o usuário no arquivo')
        else:
            print(f'Cadastro de {nome} adicionado com SUCESSO')