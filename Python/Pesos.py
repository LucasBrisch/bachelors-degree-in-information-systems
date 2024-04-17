quant = int(input("Digite a quantidade de pratos consumidos: "))
cont = 0
peso_total = 0
for prato in range(quant):
    peso = float(input("Digite o peso do prato (em Kg): "))
    peso_total = peso_total + peso
    if peso_total >= 0.8:
        cont += 1
print (f"A média de pratos por pessoa é de {peso_total / quant} kg, o total de pratos acima de 800g é de {cont}.")