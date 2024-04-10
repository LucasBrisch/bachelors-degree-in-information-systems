creditos_cartão = 0 # saldo inicial do cartão
preco_passagem = 6 # preço inicial da passagem
tentativas = 3  # tentativas de senha
senha = "admin123" # senha do administrador

#função principal, onde o usuário escolhe se é um usuário ou administrador
def main():
    global creditos_cartão, preco_passagem, tentativas #global para que as variáveis possam ser usadas em outras funções
    print()
    print("Bem-vindo ao sistema da Urbs!")
    print("você é usuário ou administrador?\n")
    print("[1] Usuário")
    print("[2] Administrador") 
    print("[3] Sair\n")
    escolha = str(input("Escolha uma opção: "))
    if escolha == '1':
        usuario()
    if escolha == '2':
        login_senha()
    if escolha == '3':
        exit()
    else:
        print("Opção inválida, tente novamente!")
        main()

    
#função do usuário que será chamada se o úsuario escolher a opção 1, ou seja, se ele for um usuário do urbs, ele poderá carregar o cartão ou fazer uma viagem
def usuario():
    global creditos_cartão, Preco_passagem  #global para chamar as variáveis que estão fora da função 
    print("Você é um usuário\n")
    print(f"Você tem R${creditos_cartão}")
    print(f"O preço da passagem é de R${preco_passagem}\n")
    print("Você deseja carregar o cartão ou fazer uma viagem?\n")
    print("[1] Carregar cartão")
    print("[2] Fazer viagem")
    print("[3] voltar para pagina inicial\n")
    escolha = str(input("Escolha uma opção: "))
    if escolha == '1':
        creditos_adicionados = int(input("Insira quantos créditos deseja colocar no cartão: "))
        creditos_cartão = creditos_cartão + creditos_adicionados
        print(f"Você adicionou R${creditos_adicionados} ao seu cartão agora você tem R${creditos_cartão}\n")
        usuario()
    elif escolha == '2':
        if creditos_cartão >= preco_passagem:
            creditos_cartão -= preco_passagem
            print(f"Você fez uma viagem! o custo foi de R${preco_passagem}")
            print(f"Agora você tem R${creditos_cartão}\n")
            usuario()
        elif creditos_cartão < preco_passagem:
            print("Você não tem créditos suficientes para fazer uma viagem, deseja carregar o cartão? \n")
            print("[1] Sim")
            print("[2] Não\n")
            escolha = str(input("Escolha uma opção: "))
            if escolha == '1':
                creditos_adicionados = int(input("insiira quantos créditos deseja colocar no cartão: "))
                creditos_cartão = creditos_cartão + creditos_adicionados
                print(f"Você adicionou R${creditos_adicionados} ao seu cartão agora você tem R${creditos_cartão}\n")
                usuario()
            elif escolha == '2':
                print("Você não pode fazer uma viagem sem créditos, volte quando quiser recarregar\n")
                usuario()
    elif escolha == '3':
        main()
        
#função de login do administrador, onde ele precisa inserir a senha para acessar as funções de administrador
def login_senha():
    global tentativas, senha
    print("Você é um administrador, favor inserir a senha para continuar")
    senha_inserida = input("(caso queira voltar, digite 'voltar')Digite a senha: ")
    if senha_inserida == "voltar":
        main()
    elif senha_inserida == senha:
            administrador()
    elif senha_inserida != senha:
        tentativas -= 1
        if tentativas == 0:
            print()
            print("Você excedeu o número de tentativas, desligando o sistema por motivos de segurança")
            exit()
        elif tentativas != 0:
            print()
            print(f"Senha incorreta, você tem mais {tentativas} tentativas restantes")    
            login_senha()


#função do administrador, onde ele pode alterar o preço da passagem ou verificar o saldo do usuário
def administrador():
    print()
    print("Bem vindo administrador! O que você deseja fazer?\n")
    print("[1] Alterar preço da passagem")
    print("[2] Verificar saldo do usuário")
    print("[3] definir uma nova senha")
    print("[4] Voltar para pagina inicial\n")
    escolha = str(input("Escolha uma opção: "))
    if escolha == '1':
        global preco_passagem
        preco_passagem = int(input("insira o novo preço da passagem: "))
        print (f"O preço da passagem agora é de R${preco_passagem}\n")
        administrador()
    elif escolha == '2':
        global creditos_cartão
        print()
        print(f"O saldo do usuario é de R${creditos_cartão}\n")
        administrador()
    elif escolha == '3':
       redefinir_senha()
    elif escolha == '4':
        main() 
    else:
        print("Opção inválida, tente novamente!\n")
        administrador()

def redefinir_senha():
    global senha
    nova_senha = input("(caso queira voltar, digite: 'voltar')Insira a nova senha: ")
    if nova_senha == "voltar":
        administrador()
    elif nova_senha == senha:
        print("A nova senha não pode ser igual a senha antiga, tente novamente")
        redefinir_senha()
    elif len(nova_senha) < 4:
        print("A senha deve ter no mínimo 4 caracteres, tente novamente")
        redefinir_senha()
    else:
        senha = nova_senha
        print("Senha redefinida com sucesso!\n")
        administrador()
    
        
if tentativas != 0:   #se o numero de tentativas for diferente de 0, o programa irá rodar, isto serve basicamente para dar o start no programa uma vez que ele sempre começa com 3 tentativas
    main()