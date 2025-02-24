import numpy as np

np.random.seed(10)

array1 = np.random.randint(1, 51, (4, 4))

for i in range(4):
    print(array1)
    print(f'Media da linha {i}: {array1[i].mean()}')
    print(f'Media da coluna {i}: {array1[:, i].mean()}')
    
print(f'Maior valor das médias das linhas: {array1.mean(axis=1).max()}')
print(f'Maior valor das médias das colunas: {array1.mean(axis=0).max()}')

unique, counts = np.unique(array1, return_counts=True)

for i in range(len(unique)):
    if counts[i] == 2:
        print(f'{unique[i]} apareceu 2 vezes')