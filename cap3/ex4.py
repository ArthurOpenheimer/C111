lista_pessoas = []
i = 0

while i != 3:
    pessoa = {}
    pessoa['nome'] = input('Entre com seu nome: ')
    pessoa['peso'] = float(input('Entre com seu peso: '))
    lista_pessoas.append(pessoa)
    i += 1

for pessoa in lista_pessoas:
    if 'mais_leve' not in locals() or pessoa['peso'] < mais_leve['peso']:
        mais_leve = pessoa
    if 'mais_pesada' not in locals() or pessoa['peso'] > mais_pesada['peso']:
        mais_pesada = pessoa

print('A pessoa mais leve é:', mais_leve['nome'])
print('A pessoa mais pesada é:', mais_pesada['nome'])