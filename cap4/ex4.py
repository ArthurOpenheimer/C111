import numpy as np

array1 = np.random.randint(0, 10, (3, 3))

rows, columns = array1.shape

if rows * columns % 2 == 0:
    print('A matriz poderia ser um vetor unidimensional com um número par de elementos')
else:
    print('A matriz poderia ser um vetor unidimensional com um número ímpar de elementos')