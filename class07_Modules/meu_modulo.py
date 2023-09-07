def exibe_nome():
    print(f'O nome deste módulo é: {__name__!r}')


if __name__ == '__main__':
    print('Olá')
    nome = input('Digite seu nome: ')
    exibe_nome()
