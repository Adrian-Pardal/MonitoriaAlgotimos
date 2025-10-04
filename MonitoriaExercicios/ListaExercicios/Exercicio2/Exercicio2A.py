

contador = 0
while True:

    if contador == 0:
        while True:
            numeroContagem = int(input("Digite o numero que quer ver a contagem : "))
            break
    contador +=1
    print(contador)

    if contador == numeroContagem:
        break
