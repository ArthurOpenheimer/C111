import numpy as np

arr = np.loadtxt('cap4/parte3/arq/space.csv', delimiter=';', dtype=str, encoding='utf-8')

locais = arr[:, 2]
locais = np.char.find(locais, 'USA')

print('Número de lançamentos nos EUA: ', np.count_nonzero(locais != -1))
