def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triângulo equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Não é um triângulo"

# Solicitar os valores ao usuário
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Verificar o tipo de triângulo
tipo_triangulo = verificar_triangulo(a, b, c)
print(tipo_triangulo)