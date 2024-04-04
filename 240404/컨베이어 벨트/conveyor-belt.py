n, t = map(int, input().split())
conveyor = [list(map(int, input().split())) for _ in range(2)]
tmp = [0] * (n * 2 + 1000)

j = 0
for i in range(n * 2):
    tmp[i] = conveyor[i // n][j]
    j += 1
    if j == n:
        j = 0

for i in range(n*2-1, -1, -1):
    tmp[i+t] = tmp[i]

for i in range(n*2-1+t, n*2-1, -1):
    tmp[i-n*2] = tmp[i]

for i in range(n * 2):
    if i == n:
        print()
    print(tmp[i], end=' ')