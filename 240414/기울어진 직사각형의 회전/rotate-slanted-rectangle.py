n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, d = map(int, input().split())

r -= 1
c -= 1

dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1] # dir == 1: reverse

i = 0
nx, ny = 0, 0
cx, cy = r, c
prev = grid[r][c]
first = grid[r][c]
for step in [m1, m2, m3, m4]:
    for _ in range(step):
        nx = cx + dx[i]
        ny = cy + dy[i]
    
        if d == 0:
            tmp = grid[nx][ny]
            grid[nx][ny] = prev
            prev = tmp
        else:
            grid[cx][cy] = grid[nx][ny]

        cx, cy = nx, ny
    i += 1

if d == 1:
    grid[r-1][c-1] = first

for g in grid:
    print(*g)