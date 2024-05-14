import random

mega = []
while len(mega) < 6:
    numero = random.randint(1, 60)
    if numero not in mega:
        mega.append(numero)
    else:
        continue
mega.sort()

cartela = []
while len(cartela) < 6:
    numero = int(input("Digite um número entre 1 e 60: "))
    if numero in cartela:
        print("Número repetido, digite outro número")
    elif numero < 1 or numero > 60:
        print("Número fora do intervalo, digite outro número")
    else:
        cartela.append(numero)
cartela.sort()

acertos = []
certos = 0        
for numero in cartela:
    if numero in mega:
        acertos.append(numero)
        certos += 1
    else:
        continue
print(f'Números sorteados: {mega}')
print(f'Números da cartela: {cartela}')
print(f'Você teve {certos} números certos: {acertos}')