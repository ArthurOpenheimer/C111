import numpy as np

paises = np.loadtxt('ex_extra/arq/paises.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

print(np.unique(paises[:, 1]))
