import math
from datetime import date
data_hoje = str(date.today()) #a data vem no formato aaaa-mm-dd, separado por hifens
print(f'Data de hoje: {data_hoje}')
#6696 são 18 anos em dias, nesse programa considerei todos os meses tendo 31 dias pra facilitar
data_nasc = input('Digite a sua data de nascimento (dd/mm/aaaa): ')
ano_atual, mes_atual, dia_atual = map(int, data_hoje.split('-')) #split so funciona com strings, por isso la em cima a variavel data_hoje foi convertida para string
dia_nasc, mes_nasc, ano_nasc = map(int, data_nasc.split('/'))
#calculo para definir a idade do usuario em dias
idade_dias = abs(((mes_atual * 31) + (ano_atual * 12 * 31) + (dia_atual)) - ((mes_nasc * 31) + (ano_nasc * 12 *31) + (dia_nasc)))

#se a idade dele ja for maior que 18 anos, ele ja pode dirigir
if idade_dias > 6696:
    print ('parabens vc tem 18 anos, vc ja pode dirigir')
#se a idade dele for menor que 18 anos, o programa calcula quantos dias faltam para ele fazer 18 anos
else:
    dias_ate_18 = abs(idade_dias - 6696)
    
    #se os dias até ele fazer 18 n forem suficientes para fechar um mes de 31 dias, o programa imprime apenas os dias
    if dias_ate_18 <31:
        print('faltam ', dias_ate_18, ' dias para você fazer 18 e poder dirigir')
    
    #se os dias forem suficientes para fechar um mes de 31 dias, o programa calcula quantos meses faltam para o usuario fazer 18 anos, e pega a sobra desse resultado para aplicar a quantidade de dias restantes
    elif dias_ate_18 >= 31:
        dias_ate_18_2 = dias_ate_18 % 31 #usar % ao inves de / para dividir, faz com q seja aplicado o valor da sobra da divisão à variavel, nesse caso, quantos dias ficam sobrando sem fechar um mes de 31 dias
        meses_ate_18 = math.trunc(dias_ate_18 / 31) #o math.trunc pega apenas o valor inteiro da divisão, no caso apenas oq vem antes da virgula
      
        #se a quantidade de meses até ele fazer 18 for menor que 12, ou seja, n é o suficiente para completar um ano, o programa imprime apenas os dias e meses
        if meses_ate_18 <12:
            print('faltam ', dias_ate_18_2, ' dias e ', meses_ate_18, 'meses para vc fazer 18')

        #se a quantidade de meses for maior que 12, o programa calcula quantos anos faltam para o usuario fazer 18 anos, e pega a sobra desse resultado para aplicar a quantidade de meses restantes, alem de resgatar a variavel q diz quantos dias faltam
        else:
            meses_ate_18_2 = meses_ate_18 % 12
            anos_ate_18 = math.trunc(meses_ate_18 / 12)
            print('faltam ', dias_ate_18_2, ' dias, ', meses_ate_18_2, ' meses e ', anos_ate_18, ' anos para vc fazer 18')
