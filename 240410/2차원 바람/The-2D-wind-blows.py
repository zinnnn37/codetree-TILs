n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1 for _ in range(m)] for __ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def shift(r1, c1, r2, c2):
    tmp = grid[r1][c1]

    for i in range(r1, r2):
        grid[i][c1] = grid[i+1][c1]
    for i in range(c1+1, c2+1):
        grid[r2][i-1] = grid[r2][i]
    for i in range(r2, r1, -1):
        grid[i][c2] = grid[i-1][c2]
    for i in range(c2, c1+1, -1):
        grid[r1][i] = grid[r1][i-1]

    grid[r1][c1+1] = tmp

def _get_avg(x, y):
    total = grid[x][y]
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            total += grid[nx][ny]
            cnt += 1

    return total // cnt

def get_avg(r1, c1, r2, c2):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            ans[i][j] = _get_avg(i, j)

for _ in range(q):
    r1, c1, r2, c2 = [x - 1 for x in map(int, input().split())]
    shift(r1, c1, r2, c2)
    get_avg(r1, c1, r2, c2)

for i in range(n):
    for j in range(m):
        if ans[i][j] == -1:
            ans[i][j] = grid[i][j]

for a in ans:
    print(*a)
print()