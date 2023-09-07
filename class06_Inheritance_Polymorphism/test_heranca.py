from heranca import Mae, Filha, Neta

print('criando objeto de Mae...')
mae = Mae(1)

print('\nCriando objeto de Filha...')
filha = Filha(1, 2)

print('\nCriando objeto de Neta...')
neta = Neta(1, 2, 3)

print('\nVizualizando os objetos')
print('mae', vars(mae))
print('filha', vars(filha))
print('neta', vars(neta))
