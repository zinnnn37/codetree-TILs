n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
for i in range(n-m+1):
    for j in range(m):
        if a[i+j] not in b:
            break
        if j == 2 and a[i+j] in b:
            cnt += 1

print(cnt)