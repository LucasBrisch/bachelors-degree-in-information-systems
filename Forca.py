import random

# A função escolher_palavra() retorna uma palavra aleatória da lista de palavras
def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'desenvolvimento', 'tecnologia', 'engenharia', 'dados', 'inteligencia', 'artificial', 'algoritmo', 'shopping']
    return random.choice(palavras)

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
        print() #print() é uma função que imprime uma linha em branco

        if len(letras_erradas) > 0:
            print('Letras erradas:', ' '.join(letras_erradas)) #join é uma função que junta os elementos de uma lista em uma string, separados por um espaço

        if tentativas == 0:
            print('Você perdeu! A palavra era', palavra)
            break

        if len(letras_corretas) == len(set(palavra)): #set é uma função que remove os elementos duplicados de uma lista
            print('Parabéns! Você acertou a palavra', palavra)
            break

        palpite = input('Digite uma letra ou a palavra inteira: ').lower()

#len é uma função que retorna o tamanho de um objeto, no caso, a palavra
#o append é uma função que adiciona um item a uma lista ou a um conjunto, no caso, o palpite a lista de acertos ou erros
        if len(palpite) == 1:
            if palpite in letras_corretas or palpite in letras_erradas:
                print('Você já tentou essa letra. Escolha outra.')
            elif palpite in palavra:
                letras_corretas.append(palpite)
            else:
                letras_erradas.append(palpite)
                tentativas -= 1
        elif len (palpite) == len(palavra):
            if palpite == palavra:
                letras_corretas = list(set(palavra))
            else:
                tentativas -= 1
        else:
            print('Palpite inválido. Tente novamente.')

        print()

jogar_forca()