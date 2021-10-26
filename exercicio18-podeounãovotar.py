AnoAtual = int (input("Digite o ano atual "))

AnoNascimento = int (input("Digite seu ano de nascimento "))

Idade=AnoAtual-AnoNascimento

if Idade<16:
  print("A idade da pessoa conresponde a: {}".format(Idade), "Você não pode votar")
else:
  print("A idade da pessoa conresponde a: {}".format(Idade), "Você  pode votar")  





