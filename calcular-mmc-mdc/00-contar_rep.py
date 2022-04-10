def contar(list):
    x = []
    for i in range(len(list)):
        j = list.count(list[i])
        x.append(j)
    return x

if __name__ == "__main__":
    list1 = [2,2,2,3,3]
    print(contar(list1))
    list2 = [5,5,6,6]
    print(contar(list2))