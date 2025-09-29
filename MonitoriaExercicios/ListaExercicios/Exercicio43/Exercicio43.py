#43) Apresentar o total da soma obtida dos cem primeiros números inteiros.


soma = 0
for x in range(1 , 100 + 1):
    soma += x


print(f"Soma de 1 a 100 é : {soma}")