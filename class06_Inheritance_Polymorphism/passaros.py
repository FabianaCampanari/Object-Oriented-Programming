class Passaro:
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        pass

    def fugir(self, destino):
        pass


#  Implentar as 2 subclasses de passaro
class PassaroAereo(Passaro):
    def voar(self):
        pass


class PassaroAquatico(Passaro):
    def nadar(self):
        pass


# Implentar a classe filha da subclasse  PassaroAereo
class PassaroDeCompanhia(PassaroAereo):
    def __init__(self, vida, ataque, defesa, companheiro):
        self.companheiro = companheiro
        super().__init__(vida, ataque, defesa)


# Implentar a classe filha da subclasse PassaroAquatico
class Pinguim(PassaroAquatico):
    def __init__(self, vida, ataque, defesa, peso):
        self.peso = peso
        super().__init__(vida, ataque, defesa)


#  Instancia Objeto
aguia = PassaroDeCompanhia(100, 300, 250, 'Fabiana')

pinguim = Pinguim(140, 80, 400, 5)


print('fim')
print(Pinguim.__mro__)

