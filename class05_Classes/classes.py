class Livro:
    def __init__(self, nome, autor):
        self.nome = nome  # Atributo de Instancia Variavel
        self.autor = autor  # Atributo de Instancia Variavel
        self.editara = 'Editora Madras'  # Atibuto de Classe Fixo
        pass

    def identidade(self):
        return (f'Sou o livro {self.nome} e estou salvo'
                f' no endereço de memoria {id(self)}')


if __name__ == '__main__':
    livro_1 = Livro('A Place Called Freedom', 'Ken Follett')
    livro_2 = Livro('The Power of the Mith', 'Joseph Campbell')

    print('livro_1:', vars(livro_1))
    print(livro_1.nome)
    print(livro_1.autor)

# print('livro_2:', vars(livro_2))
