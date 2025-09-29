#14) Solicitar salário, prestação. Se prestação for maior que 20% do salário,
#imprimir: Empréstimo não pode ser concedido. Senão imprimir empréstimo
#pode ser concedido.

salario =   float(input("Informe seu salario     : "))
prestacao = float(input("Informe a sua prestação : "))

valorPorcentagem = (20 /100) * salario
print(valorPorcentagem)
if prestacao < valorPorcentagem:
    print("Emprestimo pode ser concedido !!")

else :
    print("Emprestimo não pode ser concedido !!")

