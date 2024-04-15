n = int(input())
nums = list(map(int, input().split()))


right = 1
total = nums[0]
ans = -2e9
while right < n:
    if total < 0:
        ans = max(ans, total)
        total = 0

    total += nums[right]
    
    right += 1

ans = max(ans, total)

print(ans)