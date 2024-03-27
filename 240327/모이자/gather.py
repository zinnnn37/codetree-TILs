import sys

n = int(input())
ppl = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += ppl[j] * abs(j - i)
    if tmp < min_val:
        min_val = tmp

print(min_val)