import numpy as np

arr = np.loadtxt('cap4/parte3/arq/space.csv', delimiter=';', dtype=str, encoding='utf-8')

custo = arr[:, 6]
custo = custo[1:].astype(float)
custo = custo[custo != 0]

print(f'Custo médio: {np.mean(custo):.2f}')