


numeroCerto = 15

numeroAdivinha = None
while numeroAdivinha != numeroCerto:

    numeroAdivinha = int(input("Adivinhe um numero entre 1 a 15 : "))

    if numeroAdivinha == numeroCerto:
        print(f"Parabens acertou o numero era {numeroCerto} !!")
    else:
        print("Errado tente novamente !!")