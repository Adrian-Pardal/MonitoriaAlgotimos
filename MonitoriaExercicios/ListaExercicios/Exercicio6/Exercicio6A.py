

listaNumero = []
listaRaizNumero = []
print("|------------------------------|")
print("| CALCULADORA DE RAIZ QUADRADA |")
print("|------------------------------|")

while True:

    numero = int(input("Digite o numero : "))
    listaNumero.append(numero)
    raizQuadrada = numero ** 0.5
    listaRaizNumero.append(raizQuadrada)

    while True:
        Opcao = input("Digite (S) para sim e (N) para não : ").upper()

        if Opcao == "S" or Opcao == "N":
            break
        else:
            print("Opção invalida digite novamente")

    if Opcao == "N":
        for x in range(len(listaNumero)):
            numero = listaNumero[x]
            raiz = listaRaizNumero[x]
            print(f"O numero {numero} a sua raiz é {raiz:.2f}")
        break

