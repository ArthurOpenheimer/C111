import pandas as pd

dfPaises = pd.read_csv('cap5/parte3/arq/paises.csv', delimiter=';')

noCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]

noCoast.to_csv('cap5/parte3/arq/noCoast.csv', index=False)