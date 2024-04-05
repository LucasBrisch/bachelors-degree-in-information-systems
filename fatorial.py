fatorial = int(input("Digite um número para calcular o fatorial: "))
contador = fatorial - 1

while contador > 1:
    fatorial = fatorial * contador
    contador -= 1
    
print(f"O fatorial é {fatorial}")