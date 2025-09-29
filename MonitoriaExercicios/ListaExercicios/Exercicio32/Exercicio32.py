#32) Informe o tipo de carro (A, B e C). Informe o percurso rodado em km e
#calcule o consumo estimado, conforme o tipo, sendo (A=8, B=9 e C=12)
#km/litro

tipoCarro = input("Informe o tipo do seu carro (A, B, C ) : ")
percursoRodado = float(input("Meu informe o tamahodo percurso : "))

if tipoCarro == "A":
    consumo = percursoRodado / 8
    print(f"Seu consumo no percurso foi :  {consumo:.1f} litros ")
elif tipoCarro == "B":
    consumo = percursoRodado / 9
    print(f"Seu consumo no percurso foi :  {consumo:.1f} litros ")
elif tipoCarro == "C":
    consumo = percursoRodado / 12
    print(f"Seu consumo no percurso foi :  {consumo:.1f} litros ")
else:
    print("Esse tipo de carro não temos no sistema !!")