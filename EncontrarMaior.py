maior = 0
contador = 1

while contador <= 5:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    contador += 1

print(f"O maior número digitado foi {maior}") 