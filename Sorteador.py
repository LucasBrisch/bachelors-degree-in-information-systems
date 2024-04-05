import random
contador = 1 # variavel para começar a contagem

num_alunos = int(input("Digite o número de alunos na sala: "))
lista_alunos = []  # Lista vazia para armazenar os nomes dos alunos, facilitando a escolha aleatória

while contador <= num_alunos:
    # Enquanto o contador for menor ou igual ao número de alunos, o programa pedirá o nome de cada aluno
    nome_aluno = input(f"Digite o nome do {contador}° aluno: ")
    lista_alunos.append(nome_aluno) #append adiciona o nome do aluno à lista de alunos, se escrevermos "alunos.append('João')", João será adicionado à lista
    contador += 1 # O contador é incrementado em 1 para que o programa peça o nome do próximo aluno

# O programa embaralha a lista de alunos, para que a ordem de apresentação seja aleatória
random.shuffle (lista_alunos) 
print('a ordem da apresentação é:')

for aluno in lista_alunos: # O for é lido da seguinte forma "para cada aluno na lista de alunos faça:"
    print(aluno) # O programa imprime o nome de cada aluno, na ordem em que aparecem na lista