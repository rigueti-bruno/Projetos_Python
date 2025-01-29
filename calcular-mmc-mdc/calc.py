def decomp1(num):
    from primo import primo
    x = []
    while num > 1:
        for i in range(2, num+1):
            y = primo(i)
            if y == True and num%i == 0:
                x.append(i)
                x.sort()
                num = int(num / i)
    return x

print(decomp1(2025))