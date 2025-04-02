import pandas as pd

dfPaises = pd.read_csv('cap5/parte3/arq/paises.csv', delimiter=';')

maiorPopulacao = dfPaises[dfPaises['Population'] == dfPaises['Population'].max()]

print(maiorPopulacao[['Country', 'Region']])