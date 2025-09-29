#40) Solicitar um número entre 1 e 4. Se a pessoas digitar um número
#diferente, mostrar a mensagem "entrada inválida" e solicitar o número
#novamente. Se digitar correto mostrar o número digitado.

while True:

    numero = int(input("Digite um numero entre 1 a 4   : "))

    if numero == 1 or numero == 2 or numero == 3 or numero ==4:
        print(numero)
        break
    else:
        print("Entrada inválida !!")
