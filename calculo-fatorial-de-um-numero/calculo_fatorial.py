def fatorial(n):
    f = 1
    if n == 0:
        f = 0
    else:
        while n > 0:
            f *= n
            n -= 1
    return f

x = fatorial(int(input("Informe um numero: " )))

print(x)