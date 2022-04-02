# Código para cálculo do MDC:
def decomp(a, b):
    c = []
    c.append(a)
    c.append(b)
    c.sort()
    if c[1] % c[0] == 0:
        return c[0]
    else:
        seq = []
        div1 = 0
        div2 = 0
        d = c[0]
        e = c[1]
        while d > 1:
            for num in range(1, d + 1):
                for x in range(1, num + 1):
                    resto = num % x
                    if resto == 0:
                        div1 += 1
                        r2 = d % num
                        if div1 == 2 and r2 == 0:
                            seq.append(num)
            d = int(d / num)
        while e > 1:
            for num in range(1, e + 1):
                for x in range(1, num + 1):
                    resto = num % x
                    if resto == 0:
                        div2 += 1
                        r3 = e % num
                        if div2 == 2 and r2 == 0:
                            seq.append(num)
            e = int(e / num)
        #if div == 4 and r2 == 0 and r3 == 0:
            #seq.append(num)
            #div = (div1 + div2) / 2
            
        return seq
        #return div
a = 15
b = 25

z = decomp(a, b)
print(z)


