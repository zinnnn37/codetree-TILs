n, k = map(int, input().split())
lst = []

for _ in range(n):
    candy, pos = map(int, input().split())
    lst.append([pos, candy])
lst.sort()

left = 0
right = 0
res = 0
tmp = 0
while left < n and right < n:
    if lst[right][0] - lst[left][0] > k * 2:
        tmp -= lst[left][1]
        left += 1
    else:
        tmp += lst[right][1]
        right += 1
        res = max(res, tmp)

print(res)