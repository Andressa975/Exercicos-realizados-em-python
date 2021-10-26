numeroCarroVendidos=int(input("Digite a quantidade de carros vendidos pelo funcionário: "))
valorTotalVendas=float(input("Digite o valor total de vendas: "))
salarioFixo=float(input("Digite o valor do salário fixo: "))
comissao=float(input("Digite o valor da comissão: "))

salarioFinal=salarioFixo+ (comissao*numeroCarroVendidos) + (5/100*valorTotalVendas)

print("O salário final do vendedor é de : R$ {}".format(salarioFinal))