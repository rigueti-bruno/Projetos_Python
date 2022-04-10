# A função abaixo conta quantas vezes um item de uma lista se repete na outra:

def contar(list, list2):
    x = []
    for i in range(len(list)):
        j = list2.count(list[i])
        x.append(j)
    return x

if __name__ == "__main__":
    list1 = [2,2,2,3,3]
    list2 = [2,3]
    print(contar(list2, list1))