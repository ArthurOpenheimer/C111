import numpy as np

paises = np.loadtxt('ex_extra/arq/paises.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

avg = np.mean(paises[:, 9].astype(float))
print(f'{avg:.2f}%')

