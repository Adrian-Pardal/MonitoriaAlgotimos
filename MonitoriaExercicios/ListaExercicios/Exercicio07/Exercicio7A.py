
print("-----------------------")
print("  CALCULO DE REAJUSTE  ")
print("-----------------------")
print(" O reajuste será de 1% ")
print("-----------------------")
print("  Digite zero(0) sair  \n")

while True:

    saldo = float(input("Digite o seu saldo e veja o reajuste : "))

    if saldo <= 0 :
        print("Sistema finalizado ")
        break

    porcentagem = 1
    reajuste = ((porcentagem / 100)* saldo)

    saldoReajuste = saldo + reajuste

    print(f"Seu saldo anterior           : {saldo}")
    print(f"Valor de reajuste            : {reajuste}")
    print(f"Seu saldo atual com reajuste : {saldoReajuste}")
    print("\n")
