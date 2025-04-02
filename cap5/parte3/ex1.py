import pandas as pd

dfPaises = pd.read_csv('cap5/parte3/arq/paises.csv', delimiter=';')

oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]

print(oceania)

print(f'Quantidade de países na Oceania: {len(oceania)}')