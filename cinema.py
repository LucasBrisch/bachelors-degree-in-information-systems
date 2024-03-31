# o usuario descobre quanto de desconto ele tem, com base em quantas vezes ele foi ao cinema nesse mes
frequencia = int(input("Quantas vezes você foi ao cinema este mês? "))
preco_ingresso = 50

if frequencia == 1:
    desconto = 0.2
elif frequencia in [2, 3]:
    desconto = 0.5
elif frequencia >= 4:
    desconto = 0.7
else:
    desconto = 0

# Solicita ao usuário para inserir a quantidade de ingressos e calcula o valor total
Quantidade_ingressos = int(input("Quantos ingressos você quer comprar? "))
preco_total = Quantidade_ingressos * preco_ingresso

# Calcula o valor total com desconto caso o usuário tenha esse direito
valor_com_desconto = preco_total - (preco_total * desconto)
if desconto == 0:
    print("O valor que você vai pagar é R$", preco_total)
else:
 print("O valor a pagar com o desconto da sua fidelidade é R$", valor_com_desconto)

# Verifica se o usuário foi ao cinema com o carro e usou o estacionamento
Tem_carro = input("Você foi esta com o carro no estacionamento? (sim ou não) ")
if Tem_carro == "nao":
    print("Ok, então você não precisa pagar o estacionamento.")
    exit()
else: 
    
# Calculo do valor do estacionamento caso o usuário tenha ido ao cinema com o carro
 Estacionamento_base = 10
aumento_hora = 10
Horas = float(input("Quantas horas seu carro ficou no estacionamento do cinema? "))
Valor_total = Estacionamento_base + (Horas * aumento_hora)
Valor_estacionamento_com_desconto: float = Valor_total - (Valor_total * desconto)

# Verifica se o usuário tem desconto no estacionamento
if desconto == 0:
    print("O valor do estacionamento é R$", Valor_total)
else:
 print("O valor do estacionamento com desconto é R$", Valor_estacionamento_com_desconto)
