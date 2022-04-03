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
        
        #seq5 = []
        #for i in range(len(seq3)):
        #    for j in range(len(seq4)):
         #       if seq3[i] == seq4[j] or seq3[i] < seq4[j]:
          #          seq5.append(seq3[i])
           #     else:
            #        seq5.append(seq4[j])
        #res = list(set(seq5))
        
        res = []
        y = len(inter)
        for i in range(y):
            #while i < y:
                if seq3[i] < seq4[i]:
                    x = inter[i] ** seq3[i]
                    res.append(x)
                    print(res)
                else:
                    x = inter[i] ** seq4[i]
                    res.append(x)
                #i += 1
        #if seq3[1] < seq4[1]:
         #   x = inter[1] ** seq3[1]
          #  res.append(x)
        #else:
         #   x = inter[1] ** seq4[1]
          #  res.append(x)
            
        fin = 1
        for i in res:
            fin *= i
        re1 = a % fin
        re2 = b % fin
        if re1 == 0 and re2 == 0:
            test = 'ok'
        else:
            test = 'fail'
       
        return seq1, seq2, inter, seq3, seq4, res, fin, test
        
x = 90
y = 36
z = mdc(x, y)
print(z)