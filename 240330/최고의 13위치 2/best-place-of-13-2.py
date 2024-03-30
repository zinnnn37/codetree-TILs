n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

def add(i, j):
    return sum(matrix[i][j:j+3])

r1 = add(0, 0)
r2 = add(0, 1)

for i in range(n):
    for j in range(n-2):
        if i == 0 and (j == 0 or j == 1):
            continue
        
        tmp = add(i, j)

        if tmp > r1:
            r1 = tmp
        elif tmp > r2:
            r2 = tmp

print(r1 + r2)