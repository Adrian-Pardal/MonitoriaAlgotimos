# 26) Receber do teclado, vários números e verificar se eles são ou não
# quadrados perfeitos. O programa termina quando o usuário digitar um
# número menor ou igual a zero.

print("-----------------------------------")
print("QUAL NUMERO E UMA QUADRADO PERFEITO")
print("-----------------------------------")

while True:

    numero = int(input("Digite um numero e veja : "))

    if numero <= 0:
        print("Não e quadrado perfeito")
        break
    else:
        quadradoPerfeito = False
        for i in range(0, numero):
            if i * i == numero:
                i += 1
                quadradoPerfeito = True
                break

        if quadradoPerfeito == True:
            print(f"{numero} é um quadrado perfeito ")
        elif quadradoPerfeito == False:
            print(f"{numero} não é quadrado perfeito ")