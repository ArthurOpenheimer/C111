import numpy as np

paises = np.loadtxt('ex_extra/arq/paises.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

paises[:, 1] = np.char.strip(paises[:, 1])
paises = paises[paises[:, 1] == 'LATIN AMER. & CARIB']
maximo = np.argmax(paises[:, 8].astype(float))

print(paises[maximo, 0])