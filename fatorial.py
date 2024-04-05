fatorial = int(input("Digite um número para calcular o fatorial: "))
contador = fatorial - 1 #fatorial - 1 para que o contador comece com o número anterior ao fatorial, ex: se o usuario colocar 5, o programa começara multiplicando o 5 por 4

while contador > 1: #quando o contador for =1, o programa não precisa multiplicar mais nada, pois 1*1=1, logo ele encerra o loop
    fatorial = fatorial * contador
    contador -= 1
    
print(f"O fatorial é {fatorial}")