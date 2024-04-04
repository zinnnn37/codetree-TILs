n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for __ in range(n)]

def find_subrectangle(s, x1, y1, x2, y2):
    ret = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            ret += grid[i][j]

    return ret

def second_rectangle(x, y):
    rec2 = -1001

    for i in range(n):
        for j in range(y+1, m):
            for a in range(i, n):
                for b in range(j, m):
                    rec2 = max(rec2, find_subrectangle('r2', i, j, a, b))
    
    for i in range(x+1, n):
        for j in range(m):
            for a in range(i, n):
                for b in range(j, m):
                    rec2 = max(rec2, find_subrectangle('r2', i, j, a, b))
    
    return rec2

res = -1001
for i in range(n):
    for j in range(n):
        for a in range(i, n):
            for b in range(j, m):
                if a == n-1 and b == m-1:
                    continue
                rec1 = find_subrectangle('r1', i, j, a, b)
                rec2 = second_rectangle(i+a, j+b)
                res = max(res, rec1 + rec2)

print(res)