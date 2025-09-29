#39) Solicitar a idade de várias pessoas e imprimir: Total de pessoas com menos
#de 21 anos. Total de pessoas com mais de 50 anos. O programa termina
#quando idade for = 99.

totalPessoasMenos21 = 0
totalPessoasMais50 = 0
while True:

    idade = int(input("Digite sua idade : "))

    if idade < 21:
        totalPessoasMenos21 += 1
    if idade > 50:
        totalPessoasMais50 += 1

    if idade >= 99:
        print(f"A quantidade de pessoas com menos de 21 anood foi de : {totalPessoasMenos21}")
        print(f"A quantidade de pessoas com mais de 50 anood foi de  : {totalPessoasMais50}")
        break
