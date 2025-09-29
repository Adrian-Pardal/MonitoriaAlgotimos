#29) Ler um número inteiro e verificar se está compreendido entre 20 e 80. Se
#tiver, imprimir “parabéns”, senão imprimir “chimpanzé”.


numero = int(input("Digite um numero : "))

if numero  > 20 and numero < 80:
    print("Parabéns")
else:
    print("Chimpanzé")

