import random

def adivinhar():
    random_number = random.randint(1, 100)
    tentativas = 0
    while True:
        tentativa = int(input("Tente adivinhar o número: "))
        tentativas += 1
        if tentativa == random_number:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas")
            break
        elif tentativa < random_number:
            print("Tente um número maior")
        else:
            print("Tente um número menor")
            
adivinhar()