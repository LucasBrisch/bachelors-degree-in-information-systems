import random

def preencher_lista(tamanho_lista):
    lista = []
    for _ in range(tamanho_lista):
        lista.append(random.randint(1, 100))
    return lista

tamanho_lista = int(input("Informe o tamanho da lista: "))
lista = preencher_lista(tamanho_lista)
lista.sort()
print (lista)
for numero in lista:
    if numero % 3 == 0:
        if numero % 2 == 0:
            print(f"O {numero} é múltiplo de 3 e par")
        else:
            print (f"O {numero} é múltiplo de 3 e ímpar")    
    elif numero % 2 == 0:
        print(f"O {numero} é par")
    else:
        print(f"O {numero} é ímpar")