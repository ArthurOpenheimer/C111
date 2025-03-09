import numpy as np

arr = np.loadtxt('cap4/parte3/arq/space.csv', delimiter=';', dtype=str, encoding='utf-8')

spacex_missoes = arr[arr[:, 1] == 'SpaceX']
spacex_custos = spacex_missoes[:, 6]
spacex_custos = spacex_custos[1:].astype(float)

mais_caro = np.max(spacex_custos)

print("Valor da missão mais cara: ", mais_caro)