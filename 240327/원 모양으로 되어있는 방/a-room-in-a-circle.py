import sys

MIN = sys.maxsize

n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(n):
    res = 0
    cnt = 1
    j = (i+1) % n
    while cnt < n:
        res += nums[j] * cnt
        j = (j + 1) % n
        cnt += 1
    MIN = min(MIN, res)

print(MIN)