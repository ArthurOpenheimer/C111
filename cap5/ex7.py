import numpy as np
import pandas as pd

np.random.seed(10)
df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))
print(df)


mediaD = df.loc['D'].mean()
print(f"Média dos elementos da linha D: {mediaD:.2f}")

somaE = df.iloc[4].sum() 
print(f"Soma dos elementos da linha E: {somaE}")

