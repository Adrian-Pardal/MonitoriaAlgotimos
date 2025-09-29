estado = True
senhaLogin = None
while estado != False:

    senha = input("Digite a sua senha :")
    senhaConfirmacao = input("confirmação senha digite de nova :")

    if(senhaConfirmacao == senha):
        senhaUsuario = senha
        print("Senha adicionada com sucesso!!")
        estado = False
    else:
        print("senhas diferentes digite novamente")

while senhaUsuario != senhaLogin:

    senhaLogin = input("Digite sua senha para efetuar login : ")

    if(senhaLogin == senhaUsuario):
        print("Login efetuado com Sucesso")

    else:
        print("senha incorreta digite novamente")

if senhaLogin == senhaUsuario:
    print("--------------------------")
    print("Seja bem vindo de volta !!")
    print("--------------------------")