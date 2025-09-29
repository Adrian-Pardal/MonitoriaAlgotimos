#38) Escrever um programa, que leia valores inteiros até ser lido o valor 99.
#Quando isso acontecer o programa deverá escrever a soma e a média dos
#valores lidos.


somaTotal = 0
contador = 0

listaSequencia = []
print("---------------------------------------")
print("             SENQUENCIADOR ")
print("---------------------------------------")
print("Caso a Deseje para a sequencia digite 0")
print("---------------------------------------")
while True:

    numero = int(input("Digite o numero para sair digite( 0 ) : "))

    if numero == 0:
        break

    for x in range(1 , numero + 1):
        listaSequencia.append(x)

    print(listaSequencia)