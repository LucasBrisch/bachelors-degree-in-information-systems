def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a: #verifica se é um triângulo, somando 2 lados e verificando se são maiores que o terceiro
        if a == b == c: #verifica se todos os lados são iguais
            return "Triângulo equilátero"
        elif a == b or a == c or b == c: #verifica se apenas dois lados são iguais
            return "Triângulo isósceles"
        else: #se n se encaixar em nenhum dos 2, é escaleno
            return "Triângulo escaleno"
    else:
        return "Não é um triângulo"
# O return serve para retornar o valor da função, e o valor retornado pode ser atribuido a uma variavel

# Solicitar os valores ao usuário
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Verificar o tipo de triângulo
tipo_triangulo = verificar_triangulo(a, b, c) #chama a função verificar_triangulo para aplicar valor a variavel, a variavel vai receber o valor retornado pela função
print(tipo_triangulo)