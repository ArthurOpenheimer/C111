aluno_dict = {}

aluno_dict['nome'] = input('Digite seu nome: ')
aluno_dict['media'] = int(input('Digite sua média: '))

aluno_dict['situacao'] = 'AP' if aluno_dict['media'] >= 50 else 'RP'

print(aluno_dict)