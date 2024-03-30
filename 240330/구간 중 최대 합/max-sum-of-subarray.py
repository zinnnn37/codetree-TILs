import sys

res = -sys.maxsize

k, n = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(k-n+1):
    res = max(res, sum(nums[i:i+n]))

print(res)