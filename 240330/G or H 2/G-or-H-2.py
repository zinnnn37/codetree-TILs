n = int(input())
lst = []

for _ in range(n):
    pos, c = input().split()
    lst.append([int(pos), c])
lst.sort()

res = 0
if len(lst) != 1:
    for i in range(n):
        g, h = 0, 0

        for j in range(i, n):
            if lst[j][1] == 'G':
                g += 1
            else:
                h += 1
            
            if g == h or (g > 0 and h == 0) or (g == 0 and h > 0):
                res = max(res, lst[j][0] - lst[i][0])

print(res)