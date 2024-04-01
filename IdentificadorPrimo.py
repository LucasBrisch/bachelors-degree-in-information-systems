numero = int(input("\033[m Digite um número: "))
tot = 0
for i in range (1, numero+1):
    if numero % i == 0:
        print ('\033[32m', end=' ')
        tot += 1
    else:
        print ('\033[31m', end=' ')
    print (i, end=' ')
print(f"\n\033[m O número {numero} foi divisível {tot} vezes")
if tot == 2:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")