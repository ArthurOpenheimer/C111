import pandas as pd

dfPaises = pd.read_csv('cap5/parte3/arq/paises.csv', delimiter=';')

def mede_mortalidade(taxa):
    if taxa < 9:
        return "Balanced"
    else:
        return "Urgent"
    
dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(mede_mortalidade)
print(dfPaises)