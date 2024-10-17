votos = []
contador = -1

while contador != 0:
    escolha = int(input("Digite um valor de 0 a 6 \n"))
    if escolha == 0:
        contador = 0  
    elif escolha < 0 or escolha > 6:
        print("O valor deve ser de 0 a 6")
    else:
        match escolha:
            case 1:
                votos.append("Python")
            case 2:
                votos.append("C++")
            case 3:
                votos.append("Java")
            case 4:
                votos.append("Rust")
            case 5:
                votos.append("C#")
            case 6:
                votos.append("Outro")

print("Linguagem | Votos | Percentual")
for linguagem in set(votos):
    contagem = votos.count(linguagem)
    porcentagem = (contagem / len(votos)) * 100
    print(f"{linguagem} | {contagem} | {porcentagem:.2f}%")
print(f"Total |{len(votos)}|")
