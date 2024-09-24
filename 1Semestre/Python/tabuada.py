valor = int(input("Digite um número para ver a tabuada: "))

for i in range(0,11):
    print(f"{valor} x {i} = {valor*i}")
# O código vai pegar o valor digitado pelo usuário e multiplicar por todos os números de 0 a 10 
# mostrando o resultado de cada multiplicação. O contador vai até 11 pois o range não inclui o último número
# ou seja, deve-se colocar 11 (ou 10 + 1) para que o 10 seja incluído no range