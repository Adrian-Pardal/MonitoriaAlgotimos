#08) Informar um preço de um produto e calcular novo preço com desconto de 9%

precoProduto = float(input("Informe o  preço do produto : "))

desconto = (9 / 100) * precoProduto

descontoNoProduto = precoProduto - desconto

print(f"Seu desconto foi de {desconto} o valor atual produto fica em {descontoNoProduto}")
