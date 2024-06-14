import random
captcha = ''

for _ in range(6):
    captcha += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print(captcha)
resposta = input("Digite o captcha: ")
if resposta == captcha:
    print("Captcha correto")
else:
    print("Captcha incorreto")
    
