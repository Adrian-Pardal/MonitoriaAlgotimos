#18) Somatório. Suponha que os dados digitados são para um intervalo crescente.

numeroInicio = int(input("Digite o inicio : "))
numeroFinal =  int(input("Digite o inicio : "))

soma = 0
for x in range(numeroInicio , numeroFinal +1):
    print(x)
    soma += x

print(f"Somatório dos intevarlos é de :  {soma} ")