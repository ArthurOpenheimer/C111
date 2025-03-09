import numpy as np

arr = np.loadtxt('cap4/parte3/arq/space.csv', delimiter=';', dtype=str, encoding='utf-8')

empresas = np.unique(arr[:, 1])

for empresa in empresas:
    missoes = np.count_nonzero(arr[:, 1] == empresa)
    print("Numero de missões da {} : {}".format(empresa, missoes))