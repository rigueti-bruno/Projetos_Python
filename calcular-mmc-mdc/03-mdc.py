# Código para cálculo do MDC:
def decomp(a):
    seq = []
    while a > 1:
        for num in range(1, a + 1):
            div = 0
            r2 = a % num
            for x in range(1, num + 1):
                resto = num % x
                if resto == 0:
                    div += 1
            if div == 2 and r2 == 0:
                seq.append(num)
                a = int(a / num)
    return seq

a = 25
b = 100


x = decomp(a)
     
y = decomp(b)

for i in x:
    y.append(i)
    
m = 1
for i in y:
    m *= i
    
print(f'MDC = {m}')