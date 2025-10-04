#01) Fazer um programa que imprima a média aritmética dos números 8,9 e 7.
#A média dos números 4, 5 e 6. A soma das duas médias. A média das medias.

listaSomaNumeros1 = []
listaSomaNumeros2 = []
while True:



    for x in range(1,3 +1):
        print("Primeira parte das medias ")
        numero = float(input(f"Digite o {x}° numero da soma de 3 numeros: "))

        listaSomaNumeros1.append(numero)
    for x in range(1,3 + 1):
        print("Segunda parte das medias ")
        numero = float(input(f"Digite o {x}° numero da soma de 3 numeros: "))
        listaSomaNumeros2.append(numero)

    mediaListaSomaNumero1 = sum(listaSomaNumeros1) / len(listaSomaNumeros1)
    print(f"Media 1 :  {mediaListaSomaNumero1} ")

    mediaListaSomaNumero2 = sum(listaSomaNumeros2) / len(listaSomaNumeros2)
    print(f"Media 2 : {mediaListaSomaNumero2}")

    mediaDasMedias = (mediaListaSomaNumero1 + mediaListaSomaNumero2) / 2
    print(f"Media das medias : {mediaDasMedias}")



    while True:
        respostaOpcao = input("Quer continuar digite (S) para sim e (N) para não  : ").upper()
        if respostaOpcao == "N" or respostaOpcao == "S":
            break
        else:
            print("Opção não existe digite novamente !!")
    if respostaOpcao == "N":
        break
