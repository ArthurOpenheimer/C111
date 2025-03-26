import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25,'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21,'Python': 12.12, 'Java': 11.68})

totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print(f"Porcentagem total no ano 1 foi de {totalAno1}%")
print(f"Porcentagem total no ano 1 foi de {totalAno2}%")

