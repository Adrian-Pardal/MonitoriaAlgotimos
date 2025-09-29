#40) Solicitar um número entre 1 e 4. Se a pessoas digitar um número
#diferente, mostrar a mensagem "entrada inválida" e solicitar o número
#novamente. Se digitar correto mostrar o número digitado.

import random



while True:
    randomNumero = random.randint(1, 4)

    numero = int(input("Digite o numero de 1 a 4 : "))

    if numero == randomNumero:
        print(randomNumero)
        break
    else:
        print("Entrada inválida")
        