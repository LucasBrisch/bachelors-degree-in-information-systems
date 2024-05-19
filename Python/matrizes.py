n_Linhas = 2
n_Colunas = 2
matriz = [0] * n_Linhas
for linha in range(n_Linhas):
    matriz[linha] = [0] * n_Colunas
    
    
for linha in range(n_Linhas):
    for coluna in range(n_Colunas):
        matriz[linha][coluna] = int(input('Digite um número: '))
print(matriz)
for linha in range(n_Linhas):
    soma = 0
    for coluna in range(n_Colunas):
        soma = soma + matriz[linha][coluna]
print('Soma na linha ', linha, ' = ', soma)
