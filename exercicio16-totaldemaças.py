macas = int(input("Digite a quantidade de maças compradas: "))
if macas<12: 
    valorTotal=macas*1.3
    print("O valor total das macas corresponde a : R$ {}".format(valorTotal))
else:
    valorTotal=macas
    print("O valor total das macas corresponde a : R$ {}".format(valorTotal))