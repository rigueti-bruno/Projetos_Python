# Ferramenta de Simulação de Financiamentos
# Início
from numpy import log as ln
print('Ferramenta de Simulação de Financiamentos')
print('-------------------------------------------')
print('Ferramenta a ser utlizada para o cálculo de operações de crédito/financiamento.')
print('-------------------------------------------')
print('Instruções: \n- Insira todos os dados solicitados \n- Para o dado que não possuir, preencha 0')
print('-------------------------------------------')

# Inputs:
print('Dados:')
a = float(input("Insira a Parcela a ser paga: "))
p = float(input("Insira o Valor do Crédito a ser tomado: "))
t = float(input("Insira a Taxa de Juros da Operação: "))
i = t / 100
n = float(input("Insira o Prazo da Operação: "))

if a == 0: # Calculo da Parcela
    x = (1 + i) ** n
    y = i * x
    z = x - 1
    A = p * (y / z)                
    f = n * A    
    j = f - p    
    print(f'Condições da Operação:\n{int(n)} Parcelas de {round(A, 2)}\nValor Tomado de {round(p, 2)}\nValor Total a Pagar de {round(f, 2)}\nJuros a serem pagos de {round(j, 2)}')
elif p == 0: # Calculo do Valor Tomado
    x = (1 + i) ** n
    y = i * x
    z = x - 1
    P = a * (z / y)
    f = n * a
    j = f - P    
    print(f'Condições da Operação:\n{int(n)} Parcelas de {round(a, 2)}\nValor Tomado de {round(P, 2)}\nValor Total a Pagar de {round(f, 2)}\nJuros a serem pagos de {round(j, 2)}')
elif n == 0: # Calculo do Prazo   
    x = a - (p * i)   
    z = a / x    
    lz = ln(z)  
    y =  1 + i    
    ly = ln(y)
    N = lz / ly    
    f = N * a
    j = f - p    
    print(f'Condições da Operação:\n{int(N)} Parcelas de {round(a, 2)}\nValor Tomado de {round(p, 2)}\nValor Total a Pagar de {round(f, 2)}\nJuros a serem pagos de {round(j, 2)}')
elif i == 0: # Calculo da Taxa
    
    k = 0.0001
    I = 1    
    b = 0

    while I > 0 and b != a:
            
        x = (1 + I) ** n
        y = I * x
        z = x - 1
        b = round((p * (y / z)),2)       
        I -= k
        x = round((I * 100),2)  
    f = n * a
    j = f - p    
    print(f'Condições da Operação:\n{int(n)} Parcelas de {round(a, 2)}\nValor Tomado de {round(p, 2)}\nValor Total a Pagar de {round(f, 2)}\nJuros a serem pagos de {round(j, 2)}\nTaxa de Juros: {x}')
elif a != 0 and p != 0 and i != 0 and n != 0: # Calculo com Todos os Dados
    f = n * a
    j = f - p
    print(f'Condições da Operação:\n{int(n)} Parcelas de {round(a, 2)}\nValor Tomado de {round(p, 2)}\nValor Total a Pagar de {round(f, 2)}\nJuros a serem pagos de {round(j, 2)}\nTaxa de Juros: {t}')    