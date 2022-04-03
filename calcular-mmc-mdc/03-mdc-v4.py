def mdc(a, b):
    c = []
    c.append(a)
    c.append(b)
    c.sort()
    if c[1] % c[0] == 0:
        return c[0]
    else:
        d = c[0]
        e = c[1]
        seq1 = []
        seq2 = []
        while d > 1:
            for i in range(1, d + 1):
                div = 0
                r1 = d % i
                if r1 == 0:
                    for j in range(1, i + 1):
                        r2 = i % j
                        if r2 == 0:
                            div += 1
                if div == 2:
                    seq1.append(i) # decomposição de d
                    d = int(d / i)
        while e > 1:
            for i in range(1, e + 1):
                div = 0
                r1 = e % i
                if r1 == 0:
                    for j in range(1, i + 1):
                        r2 = i % j
                        if r2 == 0:
                            div += 1
                if div == 2:
                    seq2.append(i) # decomposição de e
                    e = int(e / i)
        inter = list((set(seq1)).intersection(set(seq2))) # fatores que se repetem nos dois
        
        seq3 = []     
        for i in range(len(inter)):
            j = seq1.count(inter[i])
            seq3.append(j)
        
        seq4 = []    
        for i in range(len(inter)):
            j = seq2.count(inter[i])
            seq4.append(j)
                     
        res = []
        y = len(inter)
        for i in range(y):            
                if seq3[i] < seq4[i]:
                    x = inter[i] ** seq3[i]
                    res.append(x)
                    print(res)
                else:
                    x = inter[i] ** seq4[i]
                    res.append(x)
      
            
        resultado = 1
        for i in res:
            resultado *= i
           
             
        return resultado
        
x = int(input('Insira o Primeiro Número: '))
y = int(input('Insira o Segundo Número: '))
z = mdc(x, y)
print(f'MDC = {z}')