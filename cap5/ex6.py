import numpy as np
import pandas as pd

np.random.seed(10)
df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))
print(df)

mediaXmenor30 = df['X'][df['X'] < 30].mean()
print(f"Média dos valores da coluna X menores que 30: {mediaXmenor30:.2f}")

