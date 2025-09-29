#13) Ler 1 número. Se positivo, imprimir raiz quadrada senão o quadrado.


numero = float(input("Digite um numero : "))

if numero > 0 :
    raizQuadrada = numero ** 0.5
    print(f"A raiz quadra do seu numero é {raizQuadrada}")
else :
    numeroQuadrado = numero ** 2
    print(f"Seu numero quadrado é {numeroQuadrado}")