nome = input("Digite seu nome completo: ")

print(nome.upper())
print(nome.lower())
print(f"{len(nome) - nome.count(' ')} letras")

nome = nome.split()
nome[-1] = "do Inatel"
nome = " ".join(nome)

print(nome)