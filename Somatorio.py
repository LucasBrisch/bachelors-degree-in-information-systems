somatorio = 0
num = int(input("Digite um número: "))

for i in range (1,num+1): # Nesse caso, o range vai de 1 até o número digitado pelo usuário
    somatorio += i
print(somatorio)
# O código acima vai somar todos os números de 1 até o número solicitado e imprimir o resultado