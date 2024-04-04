from collections import deque

n, t = map(int, input().split())
conveyor = [list(map(int, input().split())) for _ in range(3)]

q = deque()

def push():
    for _ in range(t):
        tmp = q.pop()
        q.appendleft(tmp)

i, j = 0, 0
while True:
    q.append(conveyor[i][j])
    j += 1

    if i == 2 and j == n:
        break
    elif j % n == 0:
        i += 1
        j = 0

push()

i = 0
while q:
    print(q.popleft(), end=' ')

    i += 1
    if i % n == 0:
        print()