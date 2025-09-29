#42) Fazer um programa que receba um valor n no teclado e determine o maior.
#A condição de término do programa é quando o usuário digitar zero.


maiorNumero = 0
while True:

    numero = int(input("Digite um numero : "))

    if numero > maiorNumero:
        maiorNumero = numero

    if numero == 0:
        print(f"O maior numero digitado foi : {maiorNumero}")
        break