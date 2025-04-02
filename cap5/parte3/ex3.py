import pandas as pd

dfPaises = pd.read_csv('cap5/parte3/arq/paises.csv', delimiter=';')

media = dfPaises.groupby('Region')['Literacy (%)'].mean().reset_index()

print(media)