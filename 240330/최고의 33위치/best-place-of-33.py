n = int(input())
coin = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n-2):
    for j in range(n-2):
        cnt = 0
        for k in range(3):
            cnt += coin[i+k].count(1)
        res = max(res, cnt)

print(cnt)