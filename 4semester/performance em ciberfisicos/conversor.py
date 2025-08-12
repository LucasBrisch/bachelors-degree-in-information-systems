#codigo por Lucas Brisch Zanlorenzi

decimal = input('escolha um numero decimal:')
resultado_binario = []
resultado_hexa = []
resultado_octal = []

def decimal_para_binario(decimal):
    temp = decimal % 2
    resultado_binario.append(str(temp))
    if decimal > 1:
        decimal_para_binario(decimal // 2)
    return resultado_binario

def decimal_para_octal(decimal):
    temp = decimal % 8
    resultado_octal.append(str(temp))
    if decimal > 1:
        decimal_para_binario(decimal // 8)
    return resultado_octal

def decimal_para_hexa(decimal):
    temp = decimal % 16
    
    if temp == 10:
        resultado_hexa.append('A')
    elif temp == 11:
        resultado_hexa.append('B')
    elif temp == 12:
        resultado_hexa.append('C')
    elif temp == 13:
        resultado_hexa.append('D')
    elif temp == 14:
        resultado_hexa.append('E')
    elif temp == 15:
        resultado_hexa.append('F')
    else:
        resultado_hexa.append(str(temp))
    
    if decimal > 16:
        decimal_para_hexa(decimal // 16)
    return resultado_hexa


print (decimal_para_binario(int(decimal))[::-1])
print (decimal_para_octal(int(decimal))[::-1])
print (decimal_para_hexa(int(decimal))[::-1])
