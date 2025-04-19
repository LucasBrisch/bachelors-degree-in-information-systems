# Trabalho individual realizado por Lucas Brisch Zanlorenzi

# Nesse código apenas o dono do arquivo pode deletar o mesmo e o arquivo não é deletado de vdd, ele só diz que a permissão foi concedida
# No arquivo files.json, cada arquivo possui uma serie de listas, uma lista para cada permissão, dentro dessas listas são colocados os usernames do usuarios que podem fazer a ação X no arquivo
# Por padrão, os donos dos arquivos tem todas as autorizações sobre os mesmos, caso queira privar algum usuario de fazer algo em seu proprio arquivo, deve ser alterado no files.json
# O arquivo base_de_dados.json foi criado para fins de organização, para facilitar a busca e listagem dos arquivos individuais de cada usuario quando solicitado pelo mesmo

import json

def main():
    print("1 - Login")
    print("2 - Registrar")
    
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        login()
    elif opcao == "2":
        registrar()
    else:
        print("Opção inválida. Tente novamente.")
        main()

def login():
    print("Login")
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    try:
        with open('users.json', "r") as arquivo:
            usuarios = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro ao carregar os usuários. Nenhum usuário registrado.")
        main()
        return

    for usuario in usuarios:
        if usuario["username"] == nome_usuario and usuario["password"] == senha:
            print("Login bem-sucedido!")
            tela_principal(nome_usuario)
            return

    print("Usuário ou senha inválidos.")
    login()

def registrar():
    print("Registrar")
    nome_usuario = input("Nome de usuário: ")
    if usuario_existe(nome_usuario):
        print("Usuário já existe.")
        registrar()
    else:
        senha = input("Senha: ")
        senha2 = input("Confirme a senha: ")
        if senha == senha2:
            adicionar_usuario_ao_banco(nome_usuario, senha)
            print("Usuário registrado com sucesso!")
            main()
        else:
            print("As senhas não coincidem.")
            registrar()

def usuario_existe(nome_usuario):
    try:
        with open("users.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    for usuario in usuarios:
        if usuario["username"] == nome_usuario:
            return True
    return False

def adicionar_usuario_ao_banco(nome_usuario, senha):
    try:
        with open('users.json', "r+") as arquivo:
            try:
                usuarios = json.load(arquivo)
            except json.JSONDecodeError:
                usuarios = []

            usuarios.append({"username": nome_usuario, "password": senha})
            arquivo.seek(0)
            json.dump(usuarios, arquivo, indent=4)
            arquivo.truncate()
    except FileNotFoundError:
        with open('users.json', "w") as arquivo:
            usuarios = [{"username": nome_usuario, "password": senha}]
            json.dump(usuarios, arquivo, indent=4)

    criar_base(nome_usuario)

def criar_base(nome_usuario):
    try:
        with open('base_de_dados.json', "r+") as arquivo:
            try:
                base = json.load(arquivo)
            except json.JSONDecodeError:
                base = []

            base.append({"nome": nome_usuario, "arquivos": []})
            arquivo.seek(0)
            json.dump(base, arquivo, indent=4)
            arquivo.truncate()
    except FileNotFoundError:
        with open('base_de_dados.json', "w") as arquivo:
            base = [{"nome": nome_usuario, "arquivos": []}]
            json.dump(base, arquivo, indent=4)

def tela_principal(nome_usuario):
    print("Menu Principal")
    print("1 - Criar um arquivo")
    print("2 - Ver meus arquivos")
    print("3 - Ver todos os arquivos existentes")
    print("4 - Sair")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        criar_arquivo(nome_usuario)
    elif escolha == "2":
        ver_meus_arquivos(nome_usuario)
    elif escolha == "3":
        ver_todos_arquivos(nome_usuario)
    elif escolha == "4":
        main()
    else:
        print("Por favor, escolha uma opção válida.")
        tela_principal(nome_usuario)

def criar_arquivo(nome_usuario):
    print("Por favor, escolha um nome para o seu novo arquivo:")
    nome_arquivo = input()
    
    novo_arquivo = {
        "nome": nome_arquivo,
    }

    base_geral = {
        "nome": nome_arquivo,
        "dono": nome_usuario,
        "podem_ler": [nome_usuario],
        "podem_escrever": [nome_usuario],
        "podem_executar": [nome_usuario]
    }

    try:
        with open('base_de_dados.json', 'r+') as arquivo:
            try:
                base = json.load(arquivo)
            except json.JSONDecodeError:
                base = []

            for usuario in base:
                if usuario["nome"] == nome_usuario:
                    usuario["arquivos"].append(novo_arquivo)
                    break
            else:
                print(f"Usuário '{nome_usuario}' não encontrado.")
                return

            arquivo.seek(0)
            json.dump(base, arquivo, indent=4)
            arquivo.truncate()
    except FileNotFoundError:
        print("Erro: base_de_dados.json não encontrado.")
        return

    try:
        with open('files.json', 'r+') as arquivo_files:
            try:
                files = json.load(arquivo_files)
            except json.JSONDecodeError:
                files = []

            files.append(base_geral)
            arquivo_files.seek(0)
            json.dump(files, arquivo_files, indent=4)
            arquivo_files.truncate()
    except FileNotFoundError:
        with open('files.json', 'w') as arquivo_files:
            files = [base_geral]
            json.dump(files, arquivo_files, indent=4)

    print(f"Arquivo '{nome_arquivo}' adicionado com sucesso para o usuário '{nome_usuario}'!")
    tela_principal(nome_usuario)

def verificar(acao, arquivo, nome_usuario):
    try:
        with open('files.json', 'r') as arquivo_files:
            files = json.load(arquivo_files)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro ao carregar os arquivos.")
        tela_principal(nome_usuario)
        return

    for file in files:
        if file["nome"] == arquivo:
            if acao == "deletar" and nome_usuario == file["dono"]:
                print("Permissão concedida.")
                tela_principal(nome_usuario)
            elif acao == "ler" and nome_usuario in file["podem_ler"]:
                print("Permissão concedida.")
                tela_principal(nome_usuario)
            elif acao == "editar" and nome_usuario in file["podem_escrever"]:
                print("Permissão concedida.")
                tela_principal(nome_usuario)
            elif acao == "executar" and nome_usuario in file["podem_executar"]:
                print("Permissão concedida.")
                tela_principal(nome_usuario)
            else:
                print("Permissão negada.")
                tela_principal(nome_usuario)
            return

    print("Arquivo não encontrado.")
    tela_principal(nome_usuario)

def ver_meus_arquivos(nome_usuario):
    try:
        with open('base_de_dados.json', 'r') as arquivo:
            base = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhum arquivo encontrado.")
        tela_principal(nome_usuario)
        return

    for usuario in base:
        if usuario["nome"] == nome_usuario:
            print("Seus arquivos:")
            for i, arquivo in enumerate(usuario["arquivos"], start=1):
                print(f"{i} - {arquivo['nome']}")
            break
    else:
        print("Usuário não encontrado.")
        tela_principal(nome_usuario)
        return

    escolha = input("Escolha um arquivo pelo número ou 0 para voltar: ")
    if escolha == "0":
        tela_principal(nome_usuario)
        return

    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(usuario["arquivos"]):
            arquivo_escolhido = usuario["arquivos"][escolha - 1]
            print(f"Você escolheu o arquivo: {arquivo_escolhido['nome']}")
            print("O que você deseja fazer com este arquivo?")
            print("1 - Ler")
            print("2 - Editar")
            print("3 - Executar")
            print("4 - Deletar")
            print("0 - Voltar para o menu principal")
            
            acao = input("Escolha uma ação: ")
            if acao == "0":
                tela_principal(nome_usuario)
            elif acao == "1":
                verificar("ler", arquivo_escolhido["nome"], nome_usuario)
            elif acao == "2":
                verificar("editar", arquivo_escolhido["nome"], nome_usuario)
            elif acao == "3":
                verificar("executar", arquivo_escolhido["nome"], nome_usuario)
            elif acao == "4":
                verificar("deletar", arquivo_escolhido["nome"], nome_usuario)
            else:
                print("Escolha inválida.")
                tela_principal(nome_usuario)
        else:
            print("Escolha inválida.")
            tela_principal(nome_usuario)
    except ValueError:
        print("Escolha inválida.")
        tela_principal(nome_usuario)

def ver_todos_arquivos(nome_usuario):
    try:
        with open('files.json', 'r') as arquivo:
            files = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhum arquivo encontrado.")
        tela_principal(nome_usuario)
        return

    print("Lista de todos os arquivos existentes:")
    for i, file in enumerate(files, start=1):
        print(f"{i} - {file['nome']} (Dono: {file['dono']})")

    escolha = input("Escolha um arquivo pelo número ou 0 para voltar: ")
    if escolha == "0":
        tela_principal(nome_usuario)
        return

    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(files):
            arquivo_escolhido = files[escolha - 1]
            print(f"Você escolheu o arquivo: {arquivo_escolhido['nome']}")
            print("O que você deseja fazer com este arquivo?")
            print("1 - Ler")
            print("2 - Editar")
            print("3 - Executar")
            print("4 - Deletar")
            print("0 - Voltar para o menu principal")
            
            acao = input("Escolha uma ação: ")
            if acao == "0":
                tela_principal(nome_usuario)
            elif acao == "1":
                verificar("ler", arquivo_escolhido["nome"], nome_usuario)
            elif acao == "2":
                verificar("editar", arquivo_escolhido["nome"], nome_usuario)
            elif acao == "3":
                verificar("executar", arquivo_escolhido["nome"], nome_usuario)
            elif acao == "4":
                verificar("deletar", arquivo_escolhido["nome"], nome_usuario)
            else:
                print("Escolha inválida.")
                tela_principal(nome_usuario)
        else:
            print("Escolha inválida.")
            tela_principal(nome_usuario)
    except ValueError:
        print("Escolha inválida.")
        tela_principal(nome_usuario)

main()