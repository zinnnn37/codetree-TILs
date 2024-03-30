import sys

n, h, t = map(int, input().split())
height = list(map(int, input().split()))

res = sys.maxsize
for i in range(n-t-1):
    tmp = 0
    for j in range(i, i+t):
        tmp += abs(h - height[j])
    res = min(res, tmp)

print(res)