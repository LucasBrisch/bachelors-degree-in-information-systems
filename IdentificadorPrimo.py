numero = int(input("\033[m Digite um número: "))
tot = 0
for i in range (1, numero+1):
    if numero % i == 0: # O % é o operador de módulo, ele retorna o resto da divisão, se for igual a 0, significa q o numero é divisivel por i
        print ('\033[32m', end=' ') # \033[32m é a cor verde
        tot += 1
    else:
        print ('\033[31m', end=' ') # \033[31m é a cor vermelha, usando o end=' ' para não pular linha, nesse caso, serão impressos os números que não são divisíveis na cor vermelha, para visualização do usuario
    print (i, end=' ')
    
print(f"\n\033[m O número {numero} foi divisível {tot} vezes")
if tot == 2: # se o numero foi dividido 2 vezes (1 e ele mesmo), ele é primo
    print(f"O número {numero} é primo")
else: # se for dividido mais doq 2 vezes (ou menos apenas se ele for 1) ele não é primo
    print(f"O número {numero} não é primo")
    
# Os /033[XXm são códigos de cores para o terminal, o \033[m é para resetar a cor, apenas estetico na hora de retornar o codigo
