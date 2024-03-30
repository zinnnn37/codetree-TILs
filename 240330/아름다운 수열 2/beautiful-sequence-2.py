n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()

cnt = 0
for i in range(n-m+1):
    tmp = a[i:i+m]
    tmp.sort()
    for j in range(m):
        if tmp[j] != b[j]:
            break
        
        if j == m-1 and tmp[j] == b[j]:
            cnt += 1

print(cnt)