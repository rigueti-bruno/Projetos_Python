def solution (n, ratings):
    # Write your code here
    for i in range(1,n+1):
        for j in ratings:
            grupo = {i:j}
            print(grupo)
    pass

n = int(input())
ratings = [list(map(int, input().split())) for i in range(n)]

out_ = solution(n, ratings)
print (out_)