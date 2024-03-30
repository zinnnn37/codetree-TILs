n, s = map(int, input().split())
nums = list(map(int, input().split()))

total = sum(nums)
res = 10001

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        tmp = abs(s - (total - nums[i] - nums[j]))

        if res > tmp:
            res = tmp

print(res)