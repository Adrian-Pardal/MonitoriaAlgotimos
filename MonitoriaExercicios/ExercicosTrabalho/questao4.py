#Questão 4: Entrada e Condicional
#Descrição: Escreva um programa que solicite ao usuário a idade e informe se ele pode
# votar (idade >= 18) ou não.


while True:
    print("------------------------")
    print("Será que você pode votar?")
    print("------------------------")
    idadeUsuario = int(input("Digite sua idade : "))

    if idadeUsuario >= 18:
        print("Sim e permitido em votar !!")
        break
    else :
        print("Não esta na idade de votar")
        break



