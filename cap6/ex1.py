import numpy as np
import  matplotlib.pyplot as plt

paises = np.loadtxt('cap6/arq/paises.csv', delimiter=';', dtype=str, skiprows=1)

america_norte = paises[np.char.strip(paises[:, 1]) == ('NORTHERN AMERICA')]

taxa_natalidade = america_norte[:, 15].astype(float)
taxa_mortalidade = america_norte[:, 16].astype(float)

plt.plot(taxa_natalidade, label='Taxa de Natalidade')
plt.plot(taxa_mortalidade, label='Taxa de Mortalidade')
plt.title('Taxa de Natalidade e Mortalidade na America do Norte')
plt.xlabel('Paises')
plt.ylabel('Taxa')
plt.xticks(range(len(america_norte)), america_norte[:, 0], rotation=90)
plt.show()




