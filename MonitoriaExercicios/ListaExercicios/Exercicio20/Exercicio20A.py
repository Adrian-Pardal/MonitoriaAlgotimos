#20) Apresentar o total da soma obtida dos cem primeiros números inteiros


somaTotal = 0

for x  in range(1,100 +1):
    print(x)
    somaTotal += x

print(f"A soma total dos numero de 1 a 100 é de : {somaTotal}")