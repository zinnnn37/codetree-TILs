n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_val = 0

for i in range(n):
    for j in range(n-2):
        max_val = max(max_val, matrix[i][j] + matrix[i][j+1] + matrix[i][j+2])

print(max_val)