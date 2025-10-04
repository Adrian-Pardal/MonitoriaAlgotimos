

while True:

    numero = int(input("Digite um numero e mostre o antecessor e sucessor: "))

    antecessorNumero = numero - 1
    sucessorNumero = numero + 1

    print(f"Numero escolhido foi : {numero}")
    print(f"Antecessor : {antecessorNumero}")
    print(f"Sucessor   : {sucessorNumero}")

    while True:
        respostaOpcao = input("Quer continuar digite (S) para sim e (N) para não  : ").upper()
        if respostaOpcao == "N" or respostaOpcao == "S":
            break
        else:
            print("Opção não existe digite novamente !!")
    if respostaOpcao == "N":
        break