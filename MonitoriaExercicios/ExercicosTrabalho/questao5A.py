

numerosLista = []

print("-----------------------")
print("Calculadora de media W ")
print("ate chegar um negativo")
print("-----------------------")

while True:

    numero = float(input("Digite um numero :"))

    if numero < 0:
        break

    numerosLista.append(numero)

if len(numerosLista) > 0:
    mediaPositivo = sum(numerosLista) / len(numerosLista)
    print(f"A media dos Numeros Positivos é : {mediaPositivo}")
else:
    print("Não foi digitados numeros positivos !!")

print(f"Numeros : {numerosLista}")