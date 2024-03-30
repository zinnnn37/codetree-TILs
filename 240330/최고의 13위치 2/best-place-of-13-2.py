n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

res = 0

def add(i, j):
    return sum(matrix[i][j:j+3])

for i in range(n):
    for j in range(n-2):
        tmp = add(i, j)

        for a in range(i, n):
            for b in range(n-2):
                if a == i and b <= j+2:
                    continue
                
                tmp += add(a, b)
                res = max(res, tmp)

print(res)