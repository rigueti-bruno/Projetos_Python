def primo(num):
    x = []
    y = False
    for i in range(2, num):
        if num%i == 0:
            x.append(i)
    if len(x) == 0:
        y = True
    return y

if __name__ == "__main__":
    print(primo(10))
    print(primo(13))
    print(primo(15))
    print(primo(17))