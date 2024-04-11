def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] < n :
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

num = int(input("Digite um número: "))
fib_sequence = fibonacci(num)
print(f"A sequência de Fibonacci até o número {num} é: {fib_sequence[len(fib_sequence)-2]}")