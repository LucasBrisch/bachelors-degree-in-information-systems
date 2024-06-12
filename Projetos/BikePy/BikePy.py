import math
login = "user"
senha = "1234"
creditos = 0
bicicleta_alugada = False
historico = []
data_retirada = ""
horario_retirada = ""
#definindo as variaveis globais para poderem ser acessadas em qualquer parte do programa

def main ():
    print ("Bem vindo ao BikePy")
    print ("usuário, por favor digite o seu Login: ")
    login_inserido = input ("Login: ")
    if login_inserido == login:
        print ("Usuário autenticado")
        print ()
        print ("Agora digite a sua senha: ")
        tentativas = 3
        #loop para limitar o numero de tentativas de senha
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
    else:
        print ("Usuário não encontrado")
        main()
                
def menu ():
    #menu principal do programa
    print ()
    print (f"Créditos disponíveis: {creditos}")
    print ("Menu BikePy")
    print ("O que você deseja fazer?")
    print ("1 - Adicionar créditos")
    print ("2 - Retirar bicicleta")
    print ("3 - Devolver bicicleta")
    print ("4 - Histórico de empréstimos")
    print ("5 - Sair")
    
    opcao = str(input ("Digite a opção desejada: "))
    
    #identifica a opção escolhida pelo usuário e chama a função correspondente, algumas opções possuem condições para serem executadas
    if opcao == "1":
        adicionar_creditos()
    elif opcao == "2":
        if bicicleta_alugada == True:
            print ("Você já possui uma bicicleta alugada")
            print ("Por favor devolva a bicicleta antes de alugar outra")
            menu()
        elif creditos < 5:
            print ("Créditos insuficientes, o minimo  de créditos nescessarios para alugar uma bicicleta é de 5")	
            print ("Por favor adicione créditos")
            adicionar_creditos()
        else:
            retirar_bicicleta()
    elif opcao == "3":
        if bicicleta_alugada == False:
            print ("Você não possui nenhuma bicicleta alugada")
            print ("Por favor alugue uma bicicleta antes de devolver")
            menu()
        else:
            devolver_bicicleta()
    elif opcao == "4":
        print ("Histórico de empréstimos")
        for item in historico:
            print (item)
        menu()
    elif opcao == "5":
        print ("Até logo!")
        exit()
            
            
#função para adicionar créditos à conta do usuário, o usuário pode adicionar quantos créditos quiser, desde que não seja um valor negativo
def adicionar_creditos ():
    global creditos
    print ()
    print ("Adicionar créditos")
    print ("Digite a quantidade de créditos que deseja adicionar")
    creditos_adicionados = int(input ("Créditos: "))
    if creditos_adicionados < 0:
        print ("Valor inválido, você não pode adicionar créditos negativos")
        adicionar_creditos()
    else:
        creditos += creditos_adicionados
        print (f" {creditos_adicionados} Créditos adicionados com sucesso! Cada credito vale 1 hora de aluguel de bicicleta.")
        menu()

#função para retirar a bicicleta, o usuário deve informar a data e o horário da retirada, já foi verificado se o usuário possui créditos suficientes para retirar a bicicleta
def retirar_bicicleta ():
    global data_retirada, horario_retirada
    print ("Retirar bicicleta")
    print ("Digite o dia e a hora da retirada")
    data_retirada = (input ("Dia (dd/mm/aaaa): "))
    horario_retirada = (input ("Hora (hh:mm) : "))
    print (f"Bicicleta retirada com sucesso! Data: {data_retirada} Hora: {horario_retirada}")
    
    #A variavel "bicicleta_alugada" é alterada para True, para que o programa saiba que o usuário possui uma bicicleta alugada, impedindo que ele alugue outra simultaneamente
    global bicicleta_alugada
    bicicleta_alugada = True
    menu()

#função para devolver a bicicleta, o usuário deve informar a data e o horário da devolução, o programa calcula o tempo de uso da bicicleta e desconta os créditos da conta do usuário    
def devolver_bicicleta():
    global creditos, data_retirada, horario_retirada, historico
    print ("Devolver bicicleta")
    print ("Digite o dia e a hora da devolução")
    data_devolucao = input("Dia (dd/mm/aaaa): ")
    horario_devolucao = input("Hora (hh:mm): ")
    tempo_de_uso = calcular_horas(data_devolucao, horario_devolucao, data_retirada, horario_retirada)
    print (f"Bicicleta devolvida após {tempo_de_uso} horas de uso")
    creditos -= tempo_de_uso
    print (f"Foram descontados {tempo_de_uso} créditos da sua conta")
    if creditos < 0:
        print("Infelizmente você não possui créditos suficientes para pagar o aluguel da bicicleta, logo você está devendo ao BikePy")
        print(f"Agora você tem {creditos} créditos, favor adicionar créditos para poder alugar novamente")
    else:
        print (f"Você possui {creditos} créditos restantes")
    emprestimo = "Retirada: " + data_retirada + " - "+ horario_retirada + " - Devolução: " + data_devolucao + " - "+ horario_devolucao
    historico.append(emprestimo)
        
    #a variavel "bicicleta_alugada" é alterada para False, para que o programa saiba que o usuário não possui mais uma bicicleta alugada
    global bicicleta_alugada
    bicicleta_alugada = False
    menu()


#função para calcular o tempo de uso da bicicleta, a função recebe a data e o horário da devolução e da retirada, e calcula a diferença entre eles
def calcular_horas (data_devolucao, horario_devolucao, data_retirada, horario_retirada):
    global hora_retirada, minuto_retirada, dia_retirada, mes_retirada, ano_retirada
    
    #o split separa a string em partes, o map transforma as partes em inteiros, para que assim esses valores possam ser usados em operações matemáticas
    dia_devolucao, mes_devolucao, ano_devolucao = map(int, data_devolucao.split('/'))
    hora_devolucao, minuto_devolucao = map(int, horario_devolucao.split(':'))
    
    dia_retirada, mes_retirada, ano_retirada = map(int, data_retirada.split('/'))
    hora_retirada, minuto_retirada = map(int, horario_retirada.split(':'))
    

    #transforma tudo em minutos, pra saber durante quantos minutos a bicicleta foi alugada, estão sendo usados minutos pois é a menor metrica de tempo
    tempo_minutos = ((mes_devolucao * 31 * 24 * 60) + (ano_devolucao * 12 * 31 * 24 * 60) + (dia_devolucao * 24 * 60) + (hora_devolucao * 60) + (minuto_devolucao)) - ((mes_retirada * 24 * 60 * 31) + (ano_retirada * 12 * 31 * 24 * 60) + (dia_retirada * 24 * 60) + (hora_retirada * 60) + (minuto_retirada))
    #a função abs é usada para que o resultado seja sempre positivo, independente da ordem dos valores, so para evitar erros
    #se o tempo de uso for menor que 1 hora, o programa arredonda para 1 hora com o math.ceil, ou seja, se o usuario usar a bicicleta por 1 minuto, ele paga 1 hora
    if tempo_minutos < 0:
        print ("Data de devolução inválida")
        devolver_bicicleta()
    else:
        tempo_horas = math.ceil(tempo_minutos / 60)
        return tempo_horas

    
    

main()