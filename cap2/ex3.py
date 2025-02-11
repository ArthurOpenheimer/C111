sexo = input("Digite o sexo da pessoa (M/F): ").upper()

while sexo != "M" and sexo != "F":
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    
    if sexo == "M":
        print("A pessoa é um homem")
    elif sexo == "F":
        print("A pessoa é uma mulher")