
'''Podemos concatenar strings, usando o operador + e também criar
strings formatadas de diferentes maneiras. O método recomendado
para formatação de strings em novos projetos (Bader, 2018) é chamado
de “strings literais formatadas” ou f-strings, e consiste em uma string
comum prefixada com a letra f ou F (antes da abertura das aspas)
e com os valores ou expressões que serão formatados inseridos entre
pares de chaves.'''




>>> texto = f'4 + 7 = {4 + 7},certo?'
>>> texto
'4 + 7 = 11,certo?'

'''Note que a expressão entre o par de chaves é avaliada e o resultado
inserido no mesmo ponto em que está escrita na string. A expressão é
avaliada em tempo de execução, o que permite o uso de f-strings com
variáveis e expressões, como no próximo exemplo:'''

>>> salario = 3500.0
>>> f'20% a mais em R$ {salario},dará {salario*1.2}'
'20% a mais em R$ 3500.0,dará 4200.0'

'''
No exemplo acima, seria interessante exibir os valores monetários com dua
s casas decimais. Para especificar como queremos que um valor seja formatado
em uma f-string, adicionamos : após o valor e complementamos com alguns
especificadores.'''

 
