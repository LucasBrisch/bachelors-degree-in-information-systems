# def fibonacci(n):
#     sequence = [0, 1]
#     while sequence[-1] < n :
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence

# num = int(input("Digite um número: "))
# fib_sequence = fibonacci(num)
# print(f"A sequência de Fibonacci até o número {num} é: {fib_sequence[len(fib_sequence)-2]}")

cont = int(input("quantos termos da sequencia vc quer? "))
a = 0
b = 1
fibonacci = [0, 1]

for i in range(cont - 2):
    if cont == 1 or cont == 0 or cont == 2:
        break
    else:
        c = a + b
        a = b
        b = c
        fibonacci.append (c)
print (fibonacci)