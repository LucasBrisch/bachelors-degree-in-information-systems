creditos_cartão = 0  # saldo inicial do cartão
preco_passagem = 6  # preço inicial da passagem
tentativas = 3  # tentativas de senha
senha = "admin123"  # senha do administrador

def menu_inicial():
    print()
    print("Bem-vindo ao sistema da Urbs!")
    print("Você é usuário ou administrador?\n")
    print("[1] Usuário")
    print("[2] Administrador")
    print("[3] Sair\n")
    escolha_menu = input("Escolha uma opção: ")
    return escolha_menu

def menu_usuario():
    while True:
        print("Você é um usuário\n")
        print(f"Você tem R${creditos_cartão}")
        print(f"O preço da passagem é de R${preco_passagem}\n")
        print("Você deseja carregar o cartão ou fazer uma viagem?\n")
        print("[1] Carregar cartão")
        print("[2] Fazer viagem")
        print("[3] Voltar para página inicial\n")
        escolha_user = input("Escolha uma opção: ")

        if escolha_user == '1':
            carregar_cartao()
        elif escolha_user == '2':
            fazer_viagem()
        elif escolha_user == '3':
            break
        else:
            print("Opção inválida, tente novamente!")

def carregar_cartao():
    creditos_adicionados = int(input("Quantos créditos deseja colocar no cartão? (Se deseja voltar digite '0')\n"))
    if creditos_adicionados < 0:
        print("Você não pode adicionar créditos negativos, tente novamente!\n")
    elif creditos_adicionados == 0:
        print("Voltando para o menu de usuário\n")
    else:
        global creditos_cartão
        creditos_cartão += creditos_adicionados
        print(f"Você adicionou R${creditos_adicionados} ao seu cartão agora você tem R${creditos_cartão}\n")

def fazer_viagem():
    global creditos_cartão
    if creditos_cartão >= preco_passagem:
        creditos_cartão -= preco_passagem
        print(f"Você fez uma viagem! O custo foi de R${preco_passagem}")
        print(f"Agora você tem R${creditos_cartão}\n")
    else:
        while True:
            print("Você não tem créditos suficientes para fazer uma viagem, deseja carregar o cartão? \n")
            print("[1] Sim")
            print("[2] Não\n")
            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                carregar_cartao()
                break
            elif escolha == '2':
                print("Você não pode fazer uma viagem sem créditos, volte quando quiser recarregar\n")
                break
            else:
                print("Opção inválida, tente novamente!\n")

def menu_administrador():
    volta = 0
    while volta == 0:
        print("Você é um administrador, favor inserir a senha para continuar (caso não seja um administrador, digite 'sair')")
        senha_inserida = input("Digite a senha: ")
        if senha_inserida == 'sair':
            break
        elif senha_inserida == senha:
            while True:
                print()
                print("Bem-vindo administrador! O que você deseja fazer?\n")
                print("[1] Alterar preço da passagem")
                print("[2] Verificar saldo do usuário")
                print("[3] Definir uma nova senha")
                print("[4] Voltar para página inicial\n")
                escolha_adm = input("Escolha uma opção: ")

                if escolha_adm == '1':
                    alterar_preco_passagem()
                elif escolha_adm == '2':
                    verificar_saldo_usuario()
                elif escolha_adm == '3':
                    definir_nova_senha()
                elif escolha_adm == '4':
                    volta += 1
                    break
                else:
                    print("Opção inválida, tente novamente!\n")
        else:
            global tentativas
            tentativas -= 1
            if tentativas == 0:
                print()
                print("Você excedeu o número de tentativas, desligando o sistema por motivos de segurança")
                break
            else:
                print()
                print(f"Senha incorreta, você tem mais {tentativas} tentativas restantes")

def alterar_preco_passagem():
    while True:
        novo_preco_passagem = float(input("Qual será o novo preço da passagem? (Se deseja voltar digite '0'): "))
        if novo_preco_passagem < 0:
            print("O preço da passagem não pode ser negativo, tente novamente!\n")
        elif novo_preco_passagem == 0:
            print("Voltando para o menu de administrador\n")
            break
        else:
            global preco_passagem
            preco_passagem = novo_preco_passagem
            print(f"O preço da passagem agora é de R${preco_passagem}\n")
            break

def verificar_saldo_usuario():
    print()
    print(f"O saldo do usuário é de R${creditos_cartão}\n")

def definir_nova_senha():
    while True:
        print('caso deseje voltar digite "voltar" (a senha não pode ser "voltar")')
        nova_senha = input("Insira a nova senha: ")
        if nova_senha == 'voltar':
            break
        elif nova_senha == senha:
            print("A nova senha não pode ser igual à senha antiga, tente novamente")
        elif len(nova_senha) < 4:
            print("A senha deve ter no mínimo 4 caracteres, tente novamente")
        else:
            senha = nova_senha
            print("Senha redefinida com sucesso!\n")
            break

def main():
    start = True
    while start:
        escolha_menu = menu_inicial()

        if escolha_menu == '1':
            menu_usuario()
        elif escolha_menu == '2':
            menu_administrador()
        elif escolha_menu == "3":
            print("Desligando o sistema...")
            start = False
        else:
            print("Opção inválida, tente novamente!")

main()
