colocados = ['Barcelona', 'Real Madrid', 'Santos', 'Palmeiras', 'Botafogo']

print('Os 3 primeiros colocados são:')
print(colocados[:3])

print('Os 2 últimos colocados são:')
print(colocados[-2:])

print('Times em ordem alfabética:')
print(sorted(colocados))

print('Barcelona está na posição:', colocados.index('Barcelona') + 1)