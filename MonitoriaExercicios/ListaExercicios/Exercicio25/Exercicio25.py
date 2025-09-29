#25) Um comerciante comprou um produto e quer vendê-lo com lucro de 5% se
#o valor da compra for menor que 20,00; caso contrário, o lucro será de
#30%. Entrar com o valor do produto e imprimir o valor da venda.

precoProduto = float(input("Digite o preço do produto para saber o lucro : "))

if precoProduto <= 20:
    lucro = (5 / 100) * precoProduto

    produtoMaisLucro = precoProduto + lucro
if precoProduto > 20:
    lucro = (30 / 100) * precoProduto
    produtoMaisLucro = precoProduto + lucro

print("-----------------------------")
print("      DETALHES PRODUTO")
print("-----------------------------")
print(f"Seu lucro será de : {lucro}")
print(f"O valor sem a porcemtagem : {precoProduto}")
print(f"O valor com a porcemtagem : {produtoMaisLucro}")

