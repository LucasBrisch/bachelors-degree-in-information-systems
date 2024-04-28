num_linhas = int(input("Digite o número de linhas do triângulo: "))

for i in range(0, num_linhas):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()