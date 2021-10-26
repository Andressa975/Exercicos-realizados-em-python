
nome=str(input("Digite seu nome: "))
altura=float(input("Digite sua altura"))
sexo=str(input("Digite seu sexo"))


if sexo =="F" or "f" or "Femin" or "femin" or "Feminino" or "feminino":
    pesoIdeal=72.2*altura-58
else:
pesoIdeal=62.1*altura-44.7

print("Para o sexo {} "). format(sexo), "O peso ideal é:  {}".format(pesoIdeal)


