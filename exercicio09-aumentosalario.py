salarioAtual=float(input("Digite o seu salario mensal atual: "))
percentualReajuste=float(input("Digite o percentual de reajuste: "))

# processamento
salarioFinal=salarioAtual*percentualReajuste/100+salarioAtual

print("O novo sálario com o reajuste ficou em: R$ {}".format(salarioFinal))