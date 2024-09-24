p_maior = 0
p_menor = 0
for i in range (0, 5):
    peso = float(input("Digite o peso da pessoa: "))
    if peso > p_maior:
        p_maior = peso
    if peso < p_menor or i == 0: # O i == 0 é para garantir que o primeiro peso digitado seja o menor, uma vez q n existe peso menor doq 0
        p_menor = peso
print(f"O maior peso é {p_maior} e o menor peso é {p_menor}")

# Esse codigo vai pedir o peso de 5 pessoas e vai imprimir o maior e o menor peso digitado