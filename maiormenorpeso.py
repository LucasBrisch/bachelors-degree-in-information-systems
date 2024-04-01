p_maior = 0
p_menor = 0
for i in range (0, 5):
    peso = float(input("Digite o peso da pessoa: "))
    if peso > p_maior:
        p_maior = peso
    if peso < p_menor or i == 0:
        p_menor = peso
print(f"O maior peso é {p_maior} e o menor peso é {p_menor}")