palavra = input("Digite a palavra a ser criptografada: ")
palavra_criptografada = ""
for letra in palavra:
    #o chr() retorna o caractere correspondente ao código q sera selecionado pelo ord(), ou seja palavra += a letra correspondente ao código da letra + 3
    palavra_criptografada += chr(ord(letra) + 3)
print(palavra_criptografada)