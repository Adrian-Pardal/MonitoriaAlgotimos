
somaNumeros = 0;
quantidadeInputs = 0;

print("--------------------")
print("CALCULADORA DE MEDIA")
print("--------------------")

while True:

    for x in range(1 , 3 + 1):
        numero = float(input(f"Digite o {x}° numero : "))
        somaNumeros += numero
        quantidadeInputs += 1

    media = somaNumeros / quantidadeInputs

    print(f"A soma dos numero foi   : {somaNumeros}")
    print(f"A quantidade de inputs  : {quantidadeInputs}")
    print(f"A media dos numeros foi : {media:.2f}")

    while True:
        Opcao = input("Digite (S) para continuar e (N) para encerrar :").upper()
        if Opcao == "N" or Opcao == "S":
            break
        else:
            print("Opção existe digite novamente")
    if Opcao == "N":
        break