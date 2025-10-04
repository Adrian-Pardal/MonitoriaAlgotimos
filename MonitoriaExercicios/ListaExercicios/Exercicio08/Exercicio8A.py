#08) Informar um preço de um produto e calcular novo preço com desconto de 9%

print("-----------------------")
print("  CALCULO DE REAJUSTE  ")
print("     PREÇO PRODUTO     ")
print("-----------------------")
print(" O reajuste será de 9% ")
print("-----------------------")
print("  Digite zero(0) sair  \n")

while True:

    produto = float(input("Digite o preço do produto : "))

    if produto <= 0:
        print("Sistema Finalizado !!!")
        break

    porcentagem = 9

    reajuste = (porcentagem / 100) * produto

    produtoReajuste = produto - reajuste

    print(f"Valor Reajuste             : {reajuste:.2f}")
    print(f"Preço produto sem reajuste : {produto:.2f}")
    print(f"Preço produto com reajuste : {produtoReajuste}")
    print("\n")
