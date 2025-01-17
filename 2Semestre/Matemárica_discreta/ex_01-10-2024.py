s = {2,3,4,5,6}
a = set()
b = set()
c= set()

def verificarprimo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for i in s:
    if i%2 != 0:
        a.add(i)
    if i >= 2 and i < 4:
        b.add(i)
    if  verificarprimo(i):
        c.add(i)

A_complessivo = set(a.difference(s))
B_complessivo = set(b.difference(s))
C_complessivo = set(c.difference(s))

print(a)
print(b)
print(c)

        