def s(n):
    if n == 0:
        return 1
    else:
        return s(n-1) + 1

n = int(input("Digite um número: "))
print(s(n))