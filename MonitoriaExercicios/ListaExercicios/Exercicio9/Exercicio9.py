#09) Cálculo de um salário líquido de um professor. Serão fornecidos valor da
#hora aula, numero de aulas dadas e o % de desconto do INSS.

print("__________________________")
print("Calculo do salario liquido")
print("--------------------------")
horaAula = float(input("Me informe a sua hora aula : "))
numeroAulas = int(input("Quantas aulas fez no mês  : "))
descontoINSS = float(input("Qual porcentagem do desconto do inss : "))

salarioBruto = horaAula * numeroAulas

descontoSalario =  (descontoINSS / 100) * salarioBruto

salarioLiquido = salarioBruto - descontoSalario

print(f"Sua hora aula é {horaAula} , numero de Aulas {numeroAulas} , seu desconto INSS {descontoINSS}")
print(f"Seu salario Bruto : {salarioBruto}")
print(f"Valor desconto INSS : {descontoSalario}")
print(f"Seu Liquido é de : {salarioLiquido}")