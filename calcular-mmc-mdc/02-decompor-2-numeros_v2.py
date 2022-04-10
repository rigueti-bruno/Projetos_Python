def decomp2(num1, num2):
    from primo import primo
    x = []
    while num1 > 1 and num2 > 1:
        if num1 > num2:
            z = num1
        else:
            z = num2
        for i in range(1, z + 1):
            a = primo(i)
            b = num1 % i
            c = num2 % i
            if a == True and b == 0 and c == 0:
                x.append(i)
                num1 = int(num1 / i)
                num2 = int(num2 / i)
    return x

if __name__ == "__main__":
    x = decomp2(12, 14)
    print(x)