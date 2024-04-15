# n = int(input())
# arr = list(map(int, input().split()))

# ans = -2e9
# total = 0;
# for i in range(n):
#     if total < 0:
#         total = arr[i]
#     else:
#         total += arr[i]
    
#     ans = max(ans, total)

# print(ans)

n = int(input())
nums = list(map(int, input().split()))

ans = -2e9
total = 0
for i in range(n):
    total = max(nums[i], total + nums[i])
    ans = max(ans, total)

print(total)