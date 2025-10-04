

print("-------------------------------")
print("CONVERSOR DE CELSIUS FAHRENHEIT")
print("-------------------------------")
print("    Digite (N) para sair  \n")


while True:



    celsius = int(input("Digite o grau em celsius : "))



    fahrenheit = celsius * 1.8 + 32


    print(f"Temperatura em Celsius    : {celsius}")
    print(f"Temperatura em Fahrenheit : {fahrenheit:.1f}")
    print("\n")

    Opcao = input("Digite S para continuar e N para sair : ").upper()

    if Opcao == "N":
        break
    else:
        continue