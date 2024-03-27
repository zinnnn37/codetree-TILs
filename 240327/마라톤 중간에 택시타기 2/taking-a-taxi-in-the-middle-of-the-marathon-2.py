import sys

min_val = sys.maxsize

n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]

def calc(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

total = 0
for i in range(1, n):
    prev = point[i-1]
    curr = point[i]

    total += calc(curr, prev)

for i in range(1, n-1):
    prev = point[i-1]
    curr = point[i]
    next = point[i+1]
    
    tmp = total - calc(curr, prev) - calc(next, curr) + calc(next, prev)
    
    min_val = min(min_val, tmp)

print(min_val)