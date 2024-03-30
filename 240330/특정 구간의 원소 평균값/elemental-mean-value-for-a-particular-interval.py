n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        tmp = sum(nums[i:j+1])
        avg = tmp / (j-i+1)
        if avg in nums[i:j+1]:
            cnt += 1

print(cnt)