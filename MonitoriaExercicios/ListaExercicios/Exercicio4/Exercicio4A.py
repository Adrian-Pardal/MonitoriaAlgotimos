#04) Receber um valor qualquer do teclado e imprimir esse valor com reajuste de 10%.


while True:
    numero = float(input("Digite o valor saiba o reajuste : "))

    calculoPorcentagem = (10 / 100) * numero

    reajuste = numero + calculoPorcentagem


    print(reajuste)

    while True:
        respostaOpcao = input("Quer continuar digite (S) para sim e (N) para não  : ").upper()
        if respostaOpcao == "N" or respostaOpcao == "S":
            break
        else:
            print("Opção não existe digite novamente !!")
    if respostaOpcao == "N":
        break