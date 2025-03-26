import numpy as np
import pandas as pd

np.random.seed(10)
df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))
print(df)

slicedDF = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print("Sliced DataFrame:")
print(slicedDF)

somaLinhas = slicedDF.sum(axis=1)
print("Soma dos valores de cada linha:")
print(somaLinhas)

somaLinhas = slicedDF.sum(axis=0)
print("Soma dos valores de cada coluna:")
print(somaLinhas)