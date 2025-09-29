#33) Escrever um programa que leia, valores inteiros, até ser lido o valor 99.
#Quando isso acontecer o programa deverá escrever a soma e a média dos
#valores lidos.


somaTotal = 0
quantidadeInputs = 0
while True:

    numero = int(input("Digite o proximo numero (digitando 99 mostra a soma total e media) : "))

    somaTotal += numero
    quantidadeInputs += 1

    if numero == 99:
        media = somaTotal / quantidadeInputs
        print(f"Soma total do numeros foi : {somaTotal}")
        print(f"A media do total foi de : {media:.2f}")
        break
