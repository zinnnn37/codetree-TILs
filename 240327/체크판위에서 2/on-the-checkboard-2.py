r, c = map(int, input().split())
matrix = [list(input().split()) for _ in range(r)]

start = ''
cnt = 0

if matrix[0][0] == 'W':
    start = 'W'
else:
    start = 'B'

for i in range(1, r-2):
    for j in range(1, c-2):
        if matrix[i][j] != start :
            nxt = matrix[i][j]
            for a in range(i+1, r-1):
                for b in range(j+1, c-1):
                    if matrix[a][b] != nxt:
                        if matrix[-1][-1] == nxt:
                            cnt += 1

print(cnt)