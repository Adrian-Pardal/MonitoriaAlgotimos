#Questão 3: Condicional e Repetição
#Descrição: Crie um programa que peça ao usuário para inserir uma senha.
#O programa deve solicitar uma nova senha até que o usuário insira a senha correta.
#A senha correta é "python123".


while True:

    senha = input("Digite a sua senha :")
    senhaConfirmacao = input("confirmação senha digite de nova :")

    if(senhaConfirmacao == senha):
        senhaUsuario = senha
        print("Senha adicionada com sucesso!!")
        break
    else:
        print("senhas diferentes digite novamente")

while True:

    senhaLogin = input("Digite sua senha para efetuar login : ")

    if(senhaLogin == senhaUsuario):
        print("Login efetuado com Sucesso")
        print("--------------------------")
        print("Seja bem vindo de volta !!")
        print("--------------------------")
        break
    else:
        print("senha incorreta digite novamente")





