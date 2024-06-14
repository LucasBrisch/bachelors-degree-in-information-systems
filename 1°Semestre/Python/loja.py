produtos = []
lucros = []
for i in range(100):
    produtos.append(i+1)
for produto in produtos:
    valor = float(input(f"Digite o valor do {produto}° produto: "))
    quantidade = int(input(f"Digite a quantidade de  vendas do {produto}° produto: "))
    lucros.append(valor * quantidade)
print(f'O lucro total foi de R${sum(lucros)}')