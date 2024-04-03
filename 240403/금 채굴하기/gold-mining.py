n, m = map(int, input().split())
mine = [list(map(int, input().split())) for _ in range(n)]

gold = 0

def count_gold(x, y, k):
    cnt = 0
    for i in range(-k, k+1):
        for j in range(-k + abs(i), k - abs(i) + 1): # 다이아몬드 모양으로 탐색
            nx = x + i
            ny = y + j

            if 0 <= nx < n and 0 <= ny < n and mine[nx][ny] == 1:
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        for k in range(n * 2 - 1):
            cnt = 0
            cost = k * k + (k+1) * (k+1)

            cnt += count_gold(i, j, k)

            if cnt * m >= cost:
                gold = max(gold, cnt)

print(gold)