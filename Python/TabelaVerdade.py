import ttg
vars = []
cont = int(input("Digite a quantidade de variáveis: "))
for i in range(cont):
    print("Digite o nome da variável",i+1,": ")
    vars.append(input())
equacao = []
print("Digite a equação: ")
equacao.append(input())

    
print (ttg.Truths(vars, equacao, ints=False))