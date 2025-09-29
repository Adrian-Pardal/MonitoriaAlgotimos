#Questão 6: Fatorial com Condicional e Repetição
#Descrição: Escreva um programa que peça ao usuário um número inteiro positivo e calcule o fatorial desse número. O programa deve continuar pedindo números até que o usuário insira um número negativo.
#Exemplo de saída:
#Digite um número inteiro positivo: 5
#O fatorial de 5 é: 120
#Digite um número inteiro positivo: 3
#O fatorial de 3 é: 6
#Digite um número inteiro positivo: -1
#Programa encerrado.

while True:
    numero = int(input("Digite um numero inteiro positivo : "))

    if numero < 0:
        print("Progama Encerrado")

    fatorial = 1
    for x in (range(1, numero+1)):
        fatorial *= x

    print(f"O fatorial de {numero} é :  {fatorial}")