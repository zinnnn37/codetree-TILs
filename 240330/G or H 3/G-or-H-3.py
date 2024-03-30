n, k = map(int, input().split())
lst = []

for _ in range(n):
    a, b = input().split()
    lst.append([int(a), b])

lst.sort(key=lambda x : x[0])

def GH(c):
    return 1 if c == 'G' else 2

left = 0
right = 0
res = 0
tmp = 0
while (left < n and right < n):
    if lst[right][0] - lst[left][0] + 1 > k:
        tmp -= GH(lst[left][1])
        left += 1
        res = max(res, tmp)
        continue

    tmp += GH(lst[right][1])
    res = max(res, tmp)
    right += 1

print(res)