n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

res = -1

def count(i, j, a, b):
    cnt = 0

    for c in range(i, a+1):
        for r in range(j, b+1):
            if grid[c][r] <= 0:
                return -1
            cnt += 1
    return cnt

res = -1
for i in range(n):
    for j in range(m):
        for a in range(i, n):
            for b in range(j, m):
                res = max(res, count(i, j, a, b))

print(res)