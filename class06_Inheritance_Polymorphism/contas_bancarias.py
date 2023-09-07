class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self._saldo = 0

    @property
    def saldo(self):
        return 'Seu saldo é: R$ {self._saldo}'

    def depositar(self, valor):
        self._saldo += valor
        print(f'Deposito realizado. Saldo: R$ {self._saldo}')

    def sacar(self, valor):
        if valor > self._saldo:
            print(f'Saque falhou. Saldo insuficiente: R$ {self._saldo}')
            return 0
        self._saldo -= valor
        print(f'Saque realizado. Saldo: R$ {self._saldo}')
        return valor


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular):
        self.rendimento = 0.5
        super().__init__(numero, titular)


class ContaInvestimento(ContaBancaria):
    def __init__(self, numero, titular, gerente):
        self.gerente = gerente
        super().__init__(numero, titular)

    def sacar(self, valor):
        print('verificando prazo do investimento...')
        print('calculando impostos e taxas...')
        print('realizando saque...')
        return super().sacar(valor)

    def investir(self, valor):
        print('Verificando se é possível fazer o investimento...')
        self._saldo += valor