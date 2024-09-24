import random

# A função escolher_palavra() retorna uma palavra aleatória da lista de palavras
def escolher_palavra():
    #lista de palavras, adicione quantas quiser :)
    palavras = ['python', 'programacao', 'computador', 'desenvolvimento', 'tecnologia', 'engenharia', 'dados', 'inteligencia', 'artificial', 'algoritmo', 'shopping']
    return random.choice(palavras) #seleciona uma palavra aleatoria e 'retorna' ela a variavel 'palavra', q esta em outra função

# A função jogar_forca() é como o jogo em si funciona
def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True: #while True é um loop infinito, que só para quando o break é chamado
        for letra in palavra:
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
                #nesse caso, o end=' ' é usado para não pular linha, para que os espaços sejam impressos na mesma linha
                #o codigo funciona da seguinte forma: se a letra estiver na lista de letras corretas, ela é impressa, se não, um underline é impresso
                
        print() #print() é uma função que imprime uma linha em branco, apenas estetica

        if len(letras_erradas) > 0:
            print('Letras erradas:', ' '.join(letras_erradas)) #join é uma função que junta os elementos de uma lista em uma string, separados por um espaço, q esta entre aspas
            #nesse caso, as letras erradas são impressas separadas por um espaço, e a string só é impressa se houver letras erradas

        if tentativas == 0:
            print('Você perdeu! A palavra era', palavra)
            break #break é a função que interrompe o loop, nesse caso, encerra o o jogo

        if len(letras_corretas) == len(set(palavra)): #set é uma função que remove os elementos duplicados de uma lista, ou seja, na palavra "programacao", o set(palavra) seria "progamc"
            print('Parabéns! Você acertou a palavra', palavra)
            break

        palpite = input('Digite uma letra ou a palavra inteira: ').lower() #lower é uma função que transforma a string em minúsculas, apenas estetica

#len é uma função que retorna o tamanho de um objeto, no caso, a palavra
#o append é uma função que adiciona um item a uma lista ou a um conjunto, no caso, o palpite a lista de acertos ou erros
        if len(palpite) == 1: #so roda se o palpite for uma letra
            if palpite in letras_corretas or palpite in letras_erradas: # se a letra estiver na lista de letras corretas ou erradas, o programa avisa que a letra já foi tentada
                print('Você já tentou essa letra. Escolha outra.')
            elif palpite in palavra:
                letras_corretas.append(palpite)
                #se a letra estiver na palavra, ela é adicionada a lista de letras corretas
            else:
                letras_erradas.append(palpite)
                tentativas -= 1
                #se não, ela é adicionada a lista de letras erradas e as tentativas são decrementadas
        elif len (palpite) == len(palavra): #aqui, a linha so roda se o palpite tiver a mesma quantidade de letras que a palavra
            if palpite == palavra:
                letras_corretas = list(set(palavra))
                #se o palpite for igual a palavra, ou seja, recebe todas as letras corretas, o set serve para n inserir letras repetidas
            else:
                tentativas -= 1
                print('Palavra incorreta. Tente novamente.')
        else:
            #se o palpita n for uma letra ou a palavra inteira, o programa avisa que o palpite é inválido
            print('Palpite inválido. Tente novamente.')

        print()

jogar_forca() #aqui ele esta chamando a função jogar_forca, que é a função que roda o jogo em si