import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25,'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21,'Python': 12.12, 'Java': 11.68})

variacao = ((seriesAno2 - seriesAno1) / seriesAno1) * 100

for linguagem, valor in variacao.items():
    print(f"Variação da linguagem {linguagem} foi {valor:.2f}%")

print("Linguagens com crescimento:")
for linguagem, valor in variacao.items():
    if valor > 0:
        print(f"{linguagem} com crescimento de {valor:.2f}%")
        
valoresProjetados = seriesAno2.copy()
for _ in range(2): 
    valoresProjetados += (valoresProjetados * variacao / 100)

mais_popular = valoresProjetados.nlargest(1)

print("A linguagem mais popular em 2 anos será:")
print(mais_popular)