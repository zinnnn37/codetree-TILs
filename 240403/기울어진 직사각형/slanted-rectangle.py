n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

step = [[-1, 1], [-1, -1], [1, -1], [1, 1]]

def tilted_rectangle(ix, iy, i, j, depth, total, res):
    if depth == 4:
        if ix == i and iy == j: # 원점
            res.append(total)
        return
    
    x, y = step[depth]
    nx, ny = i, j

    while True:
        px, py = nx, ny
        nx = px + x
        ny = py + y
        
        if 0 <= nx < n and 0 <= ny < n:
            total += grid[nx][ny]
            tilted_rectangle(ix, iy, nx, ny, depth+1, total, res)
        else:
            return

res = []
for i in range(n):
    for j in range(n):
        tilted_rectangle(i, j, i, j, 0, 0, res)

print(max(res))