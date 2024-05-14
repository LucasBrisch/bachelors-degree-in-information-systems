notas = []
x = 0
for i in range (5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
for nota in notas:
    x += nota
media = x / 5
print("A média do aluno é: ", media)
notas_maiores = []
for _ in notas:
    if _ > media:
        notas_maiores.append(_)
print("Notas maiores que a média: ", notas_maiores)