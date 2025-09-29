#Questão 1: Entrada, Condicional e Repetição
#Descrição: Crie um programa que peça ao usuário para inserir 5 números. Ao final,
#exiba a soma dos números que são maiores que 10.

soma= 0
for x in range(1,6):
    numero = int(input(f"Digite o {x}° numero : "))

    if numero > 10:
        soma += numero

print(soma)