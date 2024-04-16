import time

for i in range (10, 0, -1): #-1 pra deixar a contagem regressiva
    print (i) #printa o numero da vez (de 10 a 0), quando chegar a 0, ele para
    time.sleep (1) #time.sleep so para dar uma pausa de 1 segundo entre cada numero
print ("Feliz Ano Novo!")