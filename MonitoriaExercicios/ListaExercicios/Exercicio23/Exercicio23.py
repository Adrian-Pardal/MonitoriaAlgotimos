#23) Elaborar um programa que efetue a leitura de valores positivos inteiros até
#que um valor negativo seja informado. Ao final devem ser apresentados o
#maior e menor valore informados pelo usuário.

maiorNumero = 0
menorNumero = 0

while True:

    numero = int(input("Digite numeros inteiros : "))

    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero and numero > 0:
        menorNumero = numero
    if menorNumero == 0:
        menorNumero = numero

    if numero < 0 :
        break

print(f"O maioor numero digitado foi {maiorNumero} e seu menor numero foi {menorNumero}")