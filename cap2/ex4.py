dist = int(input("Digite a distância em km: "))

if dist <= 200:
    print(f"Valor da passagem em R$: {dist * 0.50}")
else:
    print(f"Valor da passagem em R$: {dist * 0.45}")