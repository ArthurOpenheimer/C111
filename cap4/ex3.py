import numpy as np

array1 = np.zeros((2, 2))

array1[np.random.randint(0, 2), np.random.randint(0, 2)] = 1

for i in range(3):
    x = int(input('Digite a linha (0 ou 1): '))
    y = int(input('Digite a coluna (0 ou 1): '))
    
    if array1[x, y] == 1:
        print('Game over! :( Try again!')
        break
    else:
        if i == 2:
            print('Congratulations! You beat the game!')
            break