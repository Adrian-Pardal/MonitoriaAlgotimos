
print("---------------------------")
print("Quer saber com quantos anos")
print("você podderá votar  ?")
print("---------------------------")
respostaUsuario = input("digite (s) para 'Sim' ou (n) para 'Não' :").lower()


while respostaUsuario == "s":
    idadeEscolhida = int(input("Digite a idade que tem duvida : "))

    tempoFaltaVotar = 18 - idadeEscolhida
    if(idadeEscolhida >= 18):
        print("Sim você ja pode votar !!")
    else:
        print(f"Não pode votar")
        print(f"Faltam {tempoFaltaVotar} anos começar a votar")

    print("---------------------------")
    print("Quer contnuar vendo com qual idade e permitido?")
    respostaUsuario = input("digite (s) para 'Sim' ou (n) para 'Não' :").lower()
    print("---------------------------")
