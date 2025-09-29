#44) Receber um número e verificar se está entre 100 e 200. Se estiver na
#faixa, imprimir: "Você digitou um número entre 100 e 200", senão estiver
#na faixa, imprimir: "Você digitou um número fora da faixa entre100 e 200".


while True:

    numero = int(input("Digite um numero entre 100 ee 200 : "))

    if numero > 100 and numero < 200:
        print(f"Você digitou um número entre 100 e 200")
    else:
        print("Você digitou um número fora da faixa entre 100 e 200")