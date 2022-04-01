# Código para a decomposição do número em Fatores Primos:

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

x = int(input('Insira um número: '))
y = decomp(x)
y.sort()
print(y)