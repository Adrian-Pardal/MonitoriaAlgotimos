#24) Receber um número do teclado e informar se ele é divisível por 10, por 5,
#por 2 ou se não é divisível por nenhum destes.

numero = float(input("Digite um numero : "))

if numero % 5 == 0 and numero % 10 == 0 and numero % 2 == 0:
    print(f"O numero {numero} é divisivel por 10 , 5 e 2")
elif numero % 5 == 0 and numero % 10 == 0 :
    print(f"O numero {numero} é divisivel por 10 e 5")
elif numero % 5 == 0 and numero % 2 == 0:
    print(f"O numero {numero} é divisivel por 5 e 2")
elif numero % 10 == 0 and numero % 2 == 0:
    print(f"O numero {numero} é divisivel por 10 e 2")
elif numero % 5 == 0 :
    print(f"O numero {numero} é divisel somente por 5")
elif numero % 10 == 0:
    print(f"O numero {numero} é divisel somente por 10")
elif numero % 2 == 0:
    print(f"O numero {numero} é divisel somente por 2")
else:
    print(f"O numero {numero} não divisel por nenhum deles .")