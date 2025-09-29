#17) Criar um algoritmo que leia os limites inferior e superior de um intervalo e
#imprimir todos os números pares no intervalo aberto e seu

limiteInferior = int(input("Digite o limite inferior : "))
limiteSuperior = int(input("Digite o limite superior : "))

listaPares = []

for x in range (limiteInferior , limiteSuperior ):
    if x % 2 == 0:
        #print(x)
        listaPares.append(x)

print(listaPares)