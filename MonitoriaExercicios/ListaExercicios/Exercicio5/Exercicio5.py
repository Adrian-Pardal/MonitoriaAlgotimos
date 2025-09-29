#05) Informar três números inteiros e imprimir a média.

somaNumeros = 0
quantidadeInputs = 0

for x in range(1,4):
    numero = float(input(f"Digite o {x}° numero : "))
    somaNumeros += numero
    quantidadeInputs += 1

media = somaNumeros / quantidadeInputs

print(f"Media dos numeros informados foi de {media}")