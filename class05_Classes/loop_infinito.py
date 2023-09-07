class Teste:
    def __init__(self):
        self.__nome = ''
        self.cont = 0

    @property
    def nome(self):
        self.cont += 1
        print('executando a @property...{self.cont}')
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        print('executando o setter...')
        self.__nome = novo_nome