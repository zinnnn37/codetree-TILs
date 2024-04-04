import copy

n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
wind = [list(input().split()) for _ in range(q)]
tmp = [0] * m

for i in range(q):
    wind[i][0] = int(wind[i][0]) - 1

def up(r, d):
    if r - 1 < 0:
        return
    for i in range(m):
        if grid[r][i] == grid[r-1][i]:
            move(r-1, d)
            up(r-1, 'L' if d == 'R' else 'R')
            break

def down(r, d):
    if r + 1 >= n:
        return

    for i in range(m):
        if grid[r][i] == grid[r+1][i]:
            move(r+1, d)
            down(r+1, 'L' if d == 'R' else 'R')
            break

def move(r, d):
    if d == 'R':
        tmp[m-1] = grid[r][0]
        for i in range(m-1):
            tmp[i] = grid[r][i+1]
        grid[r] = copy.deepcopy(tmp)

    else:
        tmp[0] = grid[r][m-1]
        for i in range(m-1):
            tmp[i+1] = grid[r][i]
        grid[r] = copy.deepcopy(tmp)

for r, d in wind:
    move(r, d)

    d = 'L' if d == 'R' else 'R'
    up(r, d)
    down(r, d)

for g in grid:
    print(*g)