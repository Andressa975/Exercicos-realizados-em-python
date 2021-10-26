horaInicio = int (input("Digite o hora de início do jogo de Xadrez:"))
horaFim = int (input("Digite o hora de fim do jogo de Xadrez:"))
duracao = horaFim - horaInicio
if duracao<0:
    duracao= duracao +24
    print("A duração do jogo de Xadrez corresponde a : {}".format(duracao), " horas")
else:
    print("A duração do jogo de Xadrez corresponde a : {}".format(duracao), " horas")