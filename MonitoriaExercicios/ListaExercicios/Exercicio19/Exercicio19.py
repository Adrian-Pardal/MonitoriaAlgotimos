#19) Apresentar os quadrados dos números inteiros de 15 a 200.


numeroInicio = 15
numeroFinal = 200

for x in range(numeroInicio , numeroFinal + 1):
    numeroQuadrado = x ** 2
    print(f"O numero quadrado de {x} é |{numeroQuadrado}|")