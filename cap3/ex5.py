lista_pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Entre com seu nome: ')
    pessoa['idade'] = int(input('Entre com sua idade: '))
    pessoa['sexo'] = input('Entre com seu sexo: ')
    lista_pessoas.append(pessoa)

    if input('Deseja continuar? (s/n) ') == 'n':
        break
    
idade_avg = sum([pessoa['idade'] for pessoa in lista_pessoas]) / len(lista_pessoas)

menos_vinte = len([pessoa for pessoa in lista_pessoas if pessoa['idade'] < 20])

print('A média de idade é:', idade_avg)
print('Pessoas com menos de 20 anos:', menos_vinte)