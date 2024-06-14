numeros = []
for i in range (10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
while True:
    escolha = int(input("Digite um número: "))
    if escolha in numeros:
        print(f'{escolha} está na lista, na posição {numeros.index(escolha) + 1}')
    else:
        print(f'{escolha} não está na lista')