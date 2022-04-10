# Código para a decomposição do número em Fatores Primos:

def decomp(x):
    seq = []
    while x > 1:
        for i in range(1, x + 1):
            div = 0
            r1 = x % i
            if r1 == 0:
                for j in range(1, i + 1):
                    r2 = i % j
                    if r2 == 0:
                        div += 1
            if div == 2:
                seq.append(i)
                x = int(x / i)
    return seq

a = int(input('Insira um número: '))
y = decomp(a)
print(y)