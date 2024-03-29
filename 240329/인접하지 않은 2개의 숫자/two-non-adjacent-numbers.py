import sys

res = -sys.maxsize

n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    for j in range(i+2, n):
        res = max(res, nums[i] + nums[j])

print(res)