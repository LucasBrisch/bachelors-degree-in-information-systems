from datetime import date, datetime
login = "user"
senha = "1234"
creditos = 0

def main ():
    print ("Bem vindo ao BikePy")
    print ("usuário, por favor digite o seu Login: ")
    login_inserido = input ("Login: ")
    if login_inserido == login:
        print ("Usuário autenticado")
        print ()
        print ("Agora digite a sua senha: ")
        tentativas = 3
        while True:
            senha_inserida = input ("Senha: ")
            if senha_inserida == senha:
                print ("Senha correta")
                print ("Bem vindo ao BikePy")
                menu()
                break
            else:
                print ("Senha incorreta, tente novamente")
                tentativas -= 1
                if tentativas == 0:
                    print ("Número de tentativas excedido")
                    exit()
                else:
                    continue
                
def menu ():
    print ()
    print (f"Créditos disponíveis: {creditos}")
    print ("Menu BikePy")
    print ("O que você deseja fazer?")
    print ("1 - Adicionar créditos")
    print ("2 - Alugar bicicleta")
    
    opcao = str(input ("Digite a opção desejada: "))
    
    if opcao == "1":
        adicionar_creditos()
    elif opcao == "2":
        if creditos < 5:
            print ("Créditos insuficientes, o minimo  de créditos nescessarios para alugar uma bicicleta é de 5")	
            print ("Por favor adicione créditos")
            adicionar_creditos()
        else:
            alugar_bicicleta()
            
def adicionar_creditos ():
    global creditos
    print ()
    print ("Adicionar créditos")
    print ("Digite a quantidade de créditos que deseja adicionar")
    creditos_adicionados = int(input ("Créditos: "))
    creditos += creditos_adicionados
    print (f" {creditos_adicionados} Créditos adicionados com sucesso!")
    menu()
    
def alugar_bicicleta ():
    global creditos
    print ()
    print ("Alugue uma bicicleta")
    
    data_hoje = str(date.today())
    ano_atual, mes_atual, dia_atual = map(int, data_hoje.split('-'))
    
    horario_atual = datetime.now().time()
    
    print (f"Data de hoje: {dia_atual}/{mes_atual}/{ano_atual}")
    print (f"Horário atual: {horario_atual.hour}:{horario_atual.minute}")
    
    devolucao = input ("Digite a data e horário de devolução (dd/mm/aaaa hh:mm): ")
    data_dev, horario_dev = devolucao.split(" ")
    dia_dev, mes_dev, ano_dev = map(int, data_dev.split('/'))
    hora_dev, minuto_dev = map(int, horario_dev.split(':'))
    horas_uso = abs(hora_dev - horario_atual.hour)
    minutos_uso = abs(minuto_dev - horario_atual.minute)
    dias_uso = abs((dia_dev - dia_atual) + ((mes_dev * 30) - (30 * mes_atual)) + (ano_dev - ano_atual))
    
    
    
main()
    
    