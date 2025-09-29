#11) Ler um número e se for maior que 20 imprimir a metade desse número.

print("VEJA SE UM NUMERO E MAIOR QUE 20")
numero = float(input("Fale um numero e veja a metade dele : "))


if numero > 20:
    metade = numero / 2
    print("Sim! esse numero e maior que 20 ")
    print(f"A metade de {numero} é : {metade}")
else:
    print("Infelizmente e seu numero e menor que 20")