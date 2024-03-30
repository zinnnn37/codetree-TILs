n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

cnt = 0 if n > 1 else 2
for i in range(n):
    # count row
    row = 1
    for j in range(1, n):
        if nums[i][j-1] == nums[i][j]:
            row += 1
        else:
            row = 1

        if row >= m:
            cnt += 1
            break
    
    # count column
    col = 1
    for j in range(1, n):
        if nums[j-1][i] == nums[j][i]:
            col += 1
        else:
            col = 1

        if col >= m:
            cnt += 1
            break

print(cnt)