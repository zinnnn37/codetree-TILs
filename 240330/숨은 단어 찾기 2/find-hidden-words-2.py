n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]
res = 0
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 'E':
                    if 0 <= nx + dx[k] < n and 0 <= ny + dy[k] < m and matrix[nx + dx[k]][ny + dy[k]] == 'E':
                        res += 1

print(res)