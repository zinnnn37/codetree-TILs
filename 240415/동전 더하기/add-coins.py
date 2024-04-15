n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

cnt = 0
for i in reversed(coin):
    if k == 0:
        break

    while k - i >= 0:
        k -= i
        cnt += 1

print(cnt)