from collections import deque

n, t = map(int, input().split())
conveyor = [list(map(int, input().split())) for _ in range(2)]

def push(q):
    for _ in range(t):
        tmp = q.pop()
        q.appendleft(tmp)

q = deque()

for i in range(2):
    for j in range(n):
        q.append(conveyor[i][j])

push(q)

for i in range(n*2):
    if i == n:
        print()
    print(q[i], end=' ')