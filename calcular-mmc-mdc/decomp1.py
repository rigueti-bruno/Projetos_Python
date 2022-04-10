# A função abaixo decompõe um número em fatores primos:

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

# A função abaixo faz o cálculo inverso da decomposição de um número:

def conf1(list):
    x = 1
    for i in list:
        x *= i
    return x

if __name__ == "__main__":
    print(decomp1(200))
    print(decomp1(150))
    print(decomp1(54))
    print(decomp1(36))
    print(decomp1(9))
    print("...")
    print(conf1(decomp1(200)))
    print(conf1(decomp1(150)))
    print(conf1(decomp1(54)))
    print(conf1(decomp1(36)))
    print(conf1(decomp1(9)))
            
            