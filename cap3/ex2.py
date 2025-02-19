loja1 = {'iphone 15', 'iphone 16', 'S20', 'Moto G9'}
loja2 = {'iphone 15', 'iphone 16', 'S20', 'S21'}

print('Todas as possíveis compras:')
print(loja1.union(loja2))

print('Modelos nas duas lojas:')
print(loja1.intersection(loja2))