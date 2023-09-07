class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor < 0:
            return 'Valor Invalido'
        self.__saldo += valor
        return 'Deposito Realizado com Sucesso'

    def sacar(self, valor):
        if valor < 0:
            return 'Valor Invalido'
        if valor > self.__saldo:
            return 'Saldo Insuficiente'
        self.__saldo -= valor
        return 'Saque Realizado com Sucesso'


if __name__ == '__main__':
    c1 = Conta(1, 'Fabiana')