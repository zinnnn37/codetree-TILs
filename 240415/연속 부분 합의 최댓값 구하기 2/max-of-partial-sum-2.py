n = int(input())
nums = list(map(int, input().split()))

total = nums[0]
ans = nums[0]

for i in range(1, n):
    total = max(nums[i], total + nums[i])
    ans = max(ans, total)

print(ans)