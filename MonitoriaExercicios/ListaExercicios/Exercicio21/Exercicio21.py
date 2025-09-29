#21) Apresentar todos os números divisíveis por 4 que sejam menores que 200.


numero = 200

for x in range(1 , 200 + 1):
    if x % 4 == 0:
        print(x)