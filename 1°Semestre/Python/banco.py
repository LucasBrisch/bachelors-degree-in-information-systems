saldo = 0

def criar_conta ():
    global saldo
    print ("Bem vindo ao BancoPy")
    print ("Para criar uma conta, por favor digite o valor inicial do saldo")
    valor_inicial = int(input ("Saldo: "))
    if valor_inicial < 0:
        print ("Valor inválido, você não pode criar uma conta com um saldo negativo")
        criar_conta()
    else:
        saldo = valor_inicial
        print ("Conta criada com sucesso")
        menu()
        
def menu ():    
    print ()
    print ("Menu BancoPy")
    print ("O que você deseja fazer?")
    print ("1 - Depositar")
    print ("2 - Sacar")
    print ("3 - Consultar saldo")
    print ("4 - Sair")
    
    opcao = str(input ("Digite a opção desejada: "))
    
    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        consultar_saldo()
    elif opcao == "4":
        print ("Até logo!")
        exit()
    else:
        print ("Opção inválida")
        menu()

def depositar ():
    global saldo
    print ()
    print ("Depositar")
    print ("Digite o valor que deseja depositar")
    valor_deposito = int(input ("Valor: "))
    if valor_deposito < 0:
        print ("Valor inválido, você não pode depositar um valor negativo")
        depositar()
    else:
        saldo += valor_deposito
        print (f"R$ {valor_deposito} depositados com sucesso")
        menu()

def sacar ():
    global saldo
    print ()
    print ("Sacar")
    print ("Digite o valor que deseja sacar")
    print (f"Seu saldo é de R${saldo}")
    valor_saque = int(input ("Valor: "))
    if valor_saque < 0:
        print ("Valor inválido, você não pode sacar um valor negativo")
        sacar()
    elif valor_saque > saldo:
        print ("Saldo insuficiente")
        sacar()
    else:
        saldo -= valor_saque
        print (f"R$ {valor_saque} sacados com sucesso")
        menu()
        
def consultar_saldo ():
    global saldo
    print ()
    print ("Consultar saldo")
    print (f"Seu saldo é de R${saldo}")
    menu()
    
criar_conta()