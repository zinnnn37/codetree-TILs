n = int(input())
nums = list(map(int, input().split()))

total = 0
for i in range(n):
    total = max(nums[i], total + nums[i])

print(total)