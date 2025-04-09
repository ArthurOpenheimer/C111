import numpy as np
import  matplotlib.pyplot as plt

missoes = np.loadtxt('cap6/arq/space.csv', delimiter=';', dtype=str, encoding='utf-8')

usa = missoes[np.char.find(missoes[:, 2], 'USA') != -1]
china = missoes[np.char.find(missoes[:, 2], 'China') != -1]

usa_empresas = np.unique(usa[:, 1])
china_empresas = np.unique(china[:, 1])

plt.bar(['USA', 'CHINA'], [len(usa_empresas), len(china_empresas)])
plt.title('Quantidade de Empresas Espaciais')
plt.xlabel('Pais')
plt.ylabel('Quantidade de Empresas')
plt.show()