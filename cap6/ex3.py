import numpy as np
import  matplotlib.pyplot as plt

missoes = np.loadtxt('cap6/arq/space.csv', delimiter=';', dtype=str, encoding='utf-8')

roscosmos = missoes[missoes[:, 1] == 'Roscosmos']
status = missoes[:, 7]

sucesso = np.count_nonzero(status == 'Success')
falha = np.count_nonzero(status == 'Failure')
porcentagem = (sucesso / (sucesso + falha)) * 100

plt.pie([sucesso, falha], labels=['Sucesso', 'Falha'], autopct='%1.1f%%')
plt.title('Porcentagem de Sucesso e Falha das Missões da Roscosmos')
plt.axis('equal')
plt.show()