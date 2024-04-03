n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

di = [
    [[0, 0], [0, 1], [0, 2]],   # 가로
    [[0, 0], [1, 0], [2, 0]],   # 세로
    [[0, 0], [0, 1], [1, 0]],   # ⌜
    [[0, 0], [0, 1], [-1, 0]],  # ⌞
    [[0, 0], [0, -1], [1, 0]],  # ⌝
    [[0, 0], [0, -1], [-1, 0]], # ⌟
]

def get_sum(i, j, d):
    tmp = 0
    for dx, dy in d:
        nx = i + dx
        ny = j + dy

        if 0 <= nx < n and 0 <= ny < m:
            tmp += nums[nx][ny]
        else: return 0

    return tmp

res = 0
for i in range(n):
    for j in range(m):
        for d in di:
            res = max(res, get_sum(i, j, d))

print(res)