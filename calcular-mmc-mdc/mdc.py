# A função abaixo calcula o MDC entre 2 números:

def mdc(num1, num2):
    from decomp1 import decomp1
    from contarrep import contar
    x = decomp1(num1)
    y = decomp1(num2)
    inter = list(set(x).intersection(set(y)))
    a = contar(inter, x)
    b = contar(inter, y)
    res = []
    z = len(inter)
    for i in range(z):
        if a[i] < b[i]:
            c = inter[i] ** a[i]
            res.append(c)
        else:
            c = inter[i] ** b[i]
            res.append(c)
    m = 1
    for i in res:
        m *= i
    return m

if __name__ == "__main__":
    print(mdc(12, 14))
    print(mdc(1000, 600))
    print(mdc(14, 12))
    print(mdc(600, 1000))
    print(mdc(90, 36))