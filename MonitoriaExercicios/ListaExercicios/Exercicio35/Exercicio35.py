#35) Receber dois números e imprimi-los em ordem crescente.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verifica a ordem e imprime
if numero1 <= numero2:
    print(f"Números em ordem crescente: {numero1}, {numero2}")
else:
    print(f"Números em ordem crescente: {numero2}, {numero1}")