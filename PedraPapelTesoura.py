import random
player_score = 0
computer_score = 0

print ("Bem Vindo! Vamos jogar Pedra, Papel e Tesoura!")

def placar():
    print("Placar atual: ")
    print(f"Jogador : {player_score} | Computador: {computer_score}")
    # Mostra o placar do jogo
    
    nova_rodada = input("Quer jogar novamente? (Sim/Nao): ").capitalize()
    if nova_rodada == "Sim" or "S":
        Jogo()
    else:
        print("Obrigado por jogar! Até a próxima!")
        exit()
    # Pergunta se o jogador deseja jogar novamente, se sim, o jogo reinicia, se não, o jogo termina

def Jogo():
    global player_score, computer_score
    player = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
    computer = random.choice(["Pedra", "Papel", "Tesoura"])
    # O computador escolhe aleatoriamente entre Pedra, Papel e Tesoura, e o jogador escreve oque deseja escolher
    
    while player not in ["Pedra", "Papel", "Tesoura"]:
        player = input("Escolha inválida! Escolha Pedra, Papel ou Tesoura: ").capitalize()
        # Evita que o jogador escolha algo diferente de Pedra, Papel ou Tesoura
    
    print(f"O computador escolheu {computer}")
    
    if player == computer:
        print(f"Empate! Ambos escolheram {player}")
        # Se o jogador e o computador escolherem a mesma coisa, o jogo termina em empate
        
    elif player == "Pedra":
        if computer == "Tesoura":
            print("Você ganhou! Pedra quebra Tesoura")
            player_score += 1
        else:
            print("Você perdeu! Papel cobre Pedra")
            computer_score += 1
        # Se o jogador escolher Pedra e o computador escolher Tesoura, o jogador ganha. Se o computador escolher Papel, o jogador perde
    
    elif player == "Papel":
        if computer == "Pedra":
            print("Você ganhou! Papel cobre Pedra")
            player_score += 1
        else:
            print("Você perdeu! Tesoura corta Papel")
            computer_score += 1
        # Se o jogador escolher Papel e o computador escolher Pedra, o jogador ganha. Se o computador escolher Tesoura, o jogador perde
        
    elif player == "Tesoura":
        if computer == "Papel":
            print("Você ganhou! Tesoura corta Papel")
            player_score += 1
        else:
            print("Você perdeu! Pedra quebra Tesoura")
            computer_score += 1
        # Se o jogador escolher Tesoura e o computador escolher Papel, o jogador ganha. Se o computador escolher Pedra, o jogador perde
    placar()

Jogo()