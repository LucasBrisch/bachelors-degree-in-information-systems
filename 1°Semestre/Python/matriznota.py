n_Linhas = 3
n_Colunas = 4
matriz = [0] * n_Linhas
for linha in range(n_Linhas):
    matriz[linha] = [0] * n_Colunas
    
for linha in range(n_Linhas):
    for coluna in range(n_Colunas):
        matriz[linha][coluna] = int(input(f'Digite as notas do {linha +1}° aluno: '))

for linha in range(n_Linhas):
    soma = sum(matriz[linha])
    media = soma / n_Colunas
    print(f'Média do {linha + 1}° aluno: {media:.2f}')
    if media >= 7:
        print(f'O {linha + 1}° aluno está aprovado.')
    else:
        print(f'O {linha + 1}° aluno está reprovado.')