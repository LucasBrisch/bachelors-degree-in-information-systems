texto = "ola mundo"
vogais = 0
espacos = 0
concoantes = 0
for letra in texto:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
    elif letra == ' ':
        espacos += 1
    elif letra not in ['a', 'e', 'i', 'o', 'u']:
        concoantes += 1
print(f'Número de consoantes: {concoantes}')
print(f'Número de vogais: {vogais}')
print(f'Número de espaços: {espacos}')