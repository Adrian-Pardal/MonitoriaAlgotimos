#27) Ler 2 valores e somar os dois. Caso a soma seja maior que 10, mostrar a
#soma.


primeiroNumero = float(input("Digite o primeiro numero : "))
segundoNumero =  float(input("Digite o segundo numero  : "))

somaNumeros = primeiroNumero + segundoNumero

if somaNumeros > 10:
    print(f"A soma de {primeiroNumero} + {segundoNumero} é : {somaNumeros}")
else:
    print("Numero não atingiu  minimo ")