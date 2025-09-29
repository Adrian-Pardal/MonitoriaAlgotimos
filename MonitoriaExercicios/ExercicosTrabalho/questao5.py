#Questão 5: Repetição e Cálculo
#Descrição: Crie um programa que peça ao usuário para inserir números até que ele digite
# um número negativo. Ao final, exiba a média dos números positivos inseridos.
#Exemplo de saída:
#Digite um número (negativo para sair): 10
#Digite um número (negativo para sair): 20
#Digite um número (negativo para sair): -5
#A média dos números positivos é: 15.0
somaNumeros = 0
quantidadeInputs = 0
print("-----------------------")
print("Calculadora de media A ")
print("ate chegar um negativo")
print("-----------------------")
while True:

    numero = float(input("Digite um numero :"))

    if(numero >= 0 ):
        somaNumeros += numero
        quantidadeInputs = quantidadeInputs + 1
    else:
        mediaPositivo = somaNumeros / quantidadeInputs

        print(f"A media de numeros Positivos é : {mediaPositivo}")
        break

