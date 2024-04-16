nome = str(input("Digite seu nome completo: "))
print (nome.upper())
print (nome.lower())
numero_letras = len(nome) - nome.count(' ') 
print (f"seu nome tem {numero_letras} letras")

# Codigo apenas para experimentar o uso de funções para alterar o texto digitado pelo usuário