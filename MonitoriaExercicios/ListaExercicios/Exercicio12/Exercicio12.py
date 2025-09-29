#12) Ler 2 números inteiros e soma-los. Se a soma for maior que 10, mostrar o
#resultado da soma.

soma = 0
for x in range(1 , 3 ):
    numero = float(input(f"Me fale o {x}° numero :"))
    soma += numero

metade = soma / 2


if soma > 10 :
    print(f"A metade de {soma} é {metade}")
else :
    print("Essse numero não e maior que 10 ")