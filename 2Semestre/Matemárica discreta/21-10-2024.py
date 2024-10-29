# def contar_letras(palavra):
#     repetidas = {}
#     for letra in palavra:
#         if letra not in repetidas:
#             repetidas[letra] = 1
#         else:
#             repetidas[letra] += 1
        
#     repetidas = {letra:contagem for letra, contagem in repetidas.items() if contagem > 1}
#     return repetidas

# print (contar_letras(""))

def verificarprimo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def func (n):
    return n**2 - n + 41

n= 41
print(f'{func(n)} é primo? {verificarprimo(func(n))}')