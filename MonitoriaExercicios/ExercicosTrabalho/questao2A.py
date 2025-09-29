#Questão 2: Repetição e Condicional
#Descrição: Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 20. O
#programa deve continuar pedindo até que o usuário acerte.
import random


numeroCerto = random.randint(1,20)

numeroAdivinha = None
while numeroAdivinha != numeroCerto:

    numeroAdivinha = int(input("Adivinhe um numero entre 1 a 20 : "))

    if numeroAdivinha == numeroCerto:
        print(f"Parabens acertou o numero era {numeroCerto} !!")
    else:
        print("Errado tente novamente !!")