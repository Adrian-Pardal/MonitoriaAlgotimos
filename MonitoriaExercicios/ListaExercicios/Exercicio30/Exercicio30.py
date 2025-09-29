#30) Ler um número do teclado e imprimir todos os números de 1 até o número
#lido. Imprimir o produto dos números.


numeroSequencia = int(input("Digite um numero para a sequencia : "))

produto= 1
produtoRecente = 0
for x in range(1 , numeroSequencia + 1):
    if produto > produtoRecente:
        produtoRecente = produto
    produto *= x
    print(f"{produtoRecente} X {x}  = {produto}")

