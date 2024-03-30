n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

res = 0

# 3*1 1*3
for i in range(n):
    for j in range(m-2):
        res = max(res, sum(nums[i][j:j+3]))

for i in range(n-2):
    for j in range(m):
        tmp = 0
        for k in range(3):
            tmp += nums[i+k][j]
        res = max(res, tmp)
    

for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                res = max(res, nums[i][j] + nums[nx][ny] + nums[dx[(nx + 1) % 4]][dy[(ny + 1) % 4]])

print(res)