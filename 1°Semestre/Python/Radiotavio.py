massa_inicial = int(input("Digite a massa inicial: "))
cont = 0
while massa_inicial >= 0.5:
    massa_inicial = massa_inicial / 2
    cont += 1
print (f"o produto levará {cont * 50} segundos para se decompor completamente.")