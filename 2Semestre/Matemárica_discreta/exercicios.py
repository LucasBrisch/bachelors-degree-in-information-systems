import matplotlib.pyplot as plt
import numpy as np

# 3. a) A função arange sria um vetor som os valores de -5 a 5 (sem insluir o 5) com progressão de 1

def funcao1grau(a, b, x_step=0.01): 
    X = np.arange(-5, 5, x_step)
    Y = a * X + b
    
    fig = plt.figure(figsize=(10, 10))
    plt.scatter(X, Y, label="Função 1° grau")
    plt.title('f(X) = ax + b')
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.legend("inicia no -5 e termina no 4")
    plt.grid(True, which="both", ls="--")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    plt.show()

# 5. a) É um grafico discreto que representa um função afim
# 5 .b) É o mesmo grafico só que ele te maior frequencia dos pontos
# 5 .c) Os pontos ficam frequentes o bastante que a função parece ser continua com o x = 0.01
# 5 .d) A função vira uma reta continua com a função plot em vez de scatter

#################################

# 7. a)

def funcao2grau(a, b, c, x_step=0.01):
    X = np.arange(-5, 5, x_step)
    Y = a * X**2 + b * X + c
    
    fig = plt.figure(figsize=(10, 10))
    plt.scatter(X, Y, label="Função 2o grau")
    plt.show()

# 7. b)

def funcaoExponencial(a, b, x_step=0.01):
    X = np.arange(-5, 5, x_step)
    Y = a * b**X
    
    fig = plt.figure(figsize=(10, 10))
    plt.scatter(X, Y, label="Função exponencial")
    plt.show()


# 7. c)

def funcaoModular (x_step=0.01):
    X = np.arange(-5, 5, x_step)
    Y = np.abs(X)
    
    fig = plt.figure(figsize=(10, 10))
    plt.scatter(X, Y, label="Função modular")
    plt.show()

# 7. d)

def funcaoSeno (x_step=0.01):
    X = np.arange(-5, 5, x_step)
    Y = np.sin(X)
    
    fig = plt.figure(figsize=(10, 10))
    plt.scatter(X, Y, label="Função seno")
    plt.show()

funcao1grau(1, 1)
funcao2grau(1, 1, 1)
funcaoExponencial(1, 2)
funcaoModular()
funcaoSeno()