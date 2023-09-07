#  Polimorfismo de sobrecarga
def sobrecarga(nome, numero=None):
    print(nome)
    if numero:
        print(numero)


print('Primeira Execução')
sobrecarga('Fabiana')

print('\nSegunda Execução')
sobrecarga('Fabiana', 10)