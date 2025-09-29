#34) Escrever um programa que receba vários números inteiros no teclado. E no
#final imprimir a média dos números múltiplos de 3. Para sair digitar 0
#(zero).

quantidadeInputs = 0
somaTotal = 0
while True:

    numero = int(input("Digite o numero e descubra se ele é multiplos de 3 : "))

    if numero % 3 == 0:
        somaTotal += numero
        quantidadeInputs += 1
        print(f"O numero {numero} multipli de 3 : ")
    else:
        print("Não e multiplo e 3")

    if numero == 0:
        break

if quantidadeInputs > 0:
    media = somaTotal / quantidadeInputs
    print(f"A média dos números múltiplos de 3 é: {media:.2f}")
else:
    print("Nenhum número múltiplo de 3 foi digitado.")