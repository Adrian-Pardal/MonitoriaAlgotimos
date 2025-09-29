#22) Elaborar um programa que efetue a leitura sucessiva de valores numéricos
#e apresente no final o total do somatório, a média e o total de valores lidos.
#O programa deve fazer as leituras dos valores enquanto o usuário estiver
#fornecendo valores positivos. Ou seja, o programa deve parar quando o
#usuário fornecer um valor negativo.


totalSomatorio = 0
quantidade = 0

print("------------------------------------------")
print("Para Encerrar se numero for menor que zero")
print("------------------------------------------")
while True:

    numero = float(input("Digite o um numero : "))

    totalSomatorio  += numero
    quantidade += 1
    if numero < 0:
        break


media = totalSomatorio / quantidade

print(f"O total dos somatorios foi {totalSomatorio} e sua media fica em {media:.2f}")