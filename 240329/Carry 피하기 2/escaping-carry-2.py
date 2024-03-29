# import sys

# res = -sys.maxsize
# n = int(input())
# nums = [int(input()) for _ in range(n)]
# total = 0

# def check_carry(x, y):
#     while True:
#         cx = x % 10
#         cy = y % 10

#         x = x // 10
#         y = y // 10

#         if cx + cy >= 10:
#             return True

#         if x == 0 or y == 0:
#             return False

# def rec(i, tmp_tal):
#     if i == n:
#         return tmp_tal
    
#     if (check_carry(nums[i], tmp_tal)):
#         return rec(i+1, tmp_tal)
#     else:
#         return max(rec(i+1, tmp_tal + nums[i]), rec(i+1, tmp_tal))

# def add():
#     for i in range(n):
#         total = max(rec(i, 0), rec(0, 0))
    
#     return total

# print(add())


import sys

res = -sys.maxsize
n = int(input())
nums = [int(input()) for _ in range(n)]

def check_carry(x, y):
    while True:
        cx = x % 10
        cy = y % 10

        x = x // 10
        y = y // 10

        if cx + cy >= 10:
            return True

        if x == 0 or y == 0:
            return False

for i in range(n):
    tmp = nums[i]
    for j in range(i, n):
        if not check_carry(tmp, nums[j]):
            tmp += nums[j]
            for k in range(j, n):
                if not check_carry(tmp, nums[k]):
                    tmp += nums[k]
                    res = max(res, tmp)

print(res)