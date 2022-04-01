# Código para a decomposição simultanea de 2 números em Fatores Primos:

def decomp2(a, b):
    seq = []
    while a > 1 and b > 1:
        if a > b:
            z = a
        else:
            z = b
        for num in range(1, z + 1):
            div = 0
            r2 = a % num
            r3 = b % num
            for x in range(1, num + 1):
                resto = num % x
                if resto == 0:
                    div += 1
            if div == 2 and r2 == 0 and r3 == 0:
                seq.append(num)
                a = int(a / num)
                b = int(b / num)
    return seq

x = 12
y = 24

z = decomp2(x, y)
z.sort()
print(z)
