def main():
    final = int(input("Digite um número para ver a sequência de Fibonacci: "))
    cont = 1
    fibbonacci = 0
    while cont  < final + 1:
        fibbonacci += cont
        cont += 1
    print(f"O número de Fibonacci é {fibbonacci}")
main()