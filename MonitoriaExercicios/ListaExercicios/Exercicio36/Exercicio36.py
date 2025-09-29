#36) Escrever um programa que receba vários números inteiros no teclado e no
#final imprimir a média dos números múltiplos de 3. Para sair digitar 0
#(zero).

somaMultiplos = 0
quantidadeInputs = 0
while True:

    numero = int(input("Digite o numero (para sair digite 0 ) : "))

    if numero % 3 == 0:
        somaMultiplos += numero
        quantidadeInputs += 1
    if numero == 0:
        mediaNumero  = somaMultiplos / quantidadeInputs
        print(f"A soma dos numeros multipplos  :  {somaMultiplos} ")
        print(f"Media dos nummeros digitados é :  {mediaNumero:.2f}")
        break