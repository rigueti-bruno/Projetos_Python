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

z =[]

for i in range(len(x)):
    for j in range(len(y)):
        if x[i] == y[j]:
            z.append(x[i])          
    
m = 1
for i in z:
    m *= i

print(x)    
print(y)
print('...')
print(z)    
print(f'MDC = {m}')