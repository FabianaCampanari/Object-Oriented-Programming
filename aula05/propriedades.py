class Teste:
    def __init__(self):
        self.__nome = 0

    @property
    def nome(self):
        print('executando a @property...')
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        print('executando o setter...')
        self.__nome = novo_nome