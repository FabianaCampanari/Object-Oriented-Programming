Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
... Podemos também construir strings com mais de uma linha utilizando três aspas seguidas (tanto simples quanto'''
'\nPodemos também construir strings com mais de uma linha utilizando três aspas seguidas (tanto simples quanto'
>>> 
>>> texto = '''Olá mundo !
... ... escrito em
...  várias linhas '''
>>> texto
'Olá mundo !\n... escrito em\n várias linhas '
>>> print(texto)
Olá mundo !
... escrito em
 várias linhas

 
# Observe que as quebras de linha são mantidas e representadas pelo caractere
# \n. Dizemos que a contra barra \ é usada para escapara letra n, dando a ela
# um significado especial, que representa uma quebra de linha.
