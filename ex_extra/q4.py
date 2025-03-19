import numpy as np

paises = np.loadtxt('ex_extra/arq/paises.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

paises[:, 1] = np.char.strip(paises[:, 1])
print(np.sum(paises[:, 1] == 'NORTHERN AMERICA'))
