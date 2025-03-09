import numpy as np

arr = np.loadtxt('cap4/parte3/arq/space.csv', delimiter=';', dtype=str, encoding='utf-8')

status = arr[:, 7]
sucesso = np.count_nonzero(status == 'Success')
falha = np.count_nonzero(status == 'Failure')

porcentagem = (sucesso / (sucesso + falha)) * 100

print(f'Porcentagem de sucesso: {porcentagem:.2f} %')
