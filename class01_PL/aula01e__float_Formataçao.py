
>>> salario = 3500.0
>>> f'20% a mais em R$ {salario},dará {salario*1.2}'
'20% a mais em R$ 3500.0,dará 4200.0'


'''
No exemplo acima, seria interessante exibir os valores monetários com dua
s casas decimais. Para especificar como queremos que um valor seja formatado
em uma f-string, adicionamos : após o valor e complementamos com alguns
especificadores.'''


#Para formatar um dado do tipo float, podemos usar o seguinte padrão de formatação:
    # f'{<valor>:<colunas>.<decimais>f}'

    
>>> pi = 3.14159265
>>> f'{pi:f}'  # sem especificar, o padrão é de 6 casas decimais
'3.141593'
>>> f'{pi:.3f}'  # note o arredondamento na última casa decimal
'3.142'
>>> f'{pi:7.3f}'  # 7 colunas totais, 3 casas decimais
'  3.142' 
