import sys

min_val = sys.maxsize

n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(1, n):
    prev = point[i-1]
    curr = point[i]

    total += abs(curr[0] - prev[0]) + abs(curr[1] - prev[1])

for i in range(1, n-1):
    prev = point[i-1]
    curr = point[i]
    next = point[i+1]
    
    tmp = total - (abs(curr[0] - prev[0]) + abs(curr[1] - prev[1])) - (abs(next[0] - curr[0]) + abs(next[1] - curr[1])) + (abs(next[0] - prev[0] + abs(next[1] - prev[1])))
    
    min_val = min(min_val, tmp)

print(min_val)