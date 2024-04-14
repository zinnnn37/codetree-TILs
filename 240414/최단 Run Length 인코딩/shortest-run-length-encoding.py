from collections import deque

s = deque(input())
res = s[0]
ans = 11
n = 0
shift = 0
shift_min = 123

while n < len(s):
    while n < len(s) and s[0] == s[-1]:
        s.appendleft(s.pop())
        n += 1
        shift += 1

    cnt = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            res += str(cnt)
            res += s[i]
            cnt = 1

    res += str(cnt)

    if shift < shift_min:
        ans = len(res)
        shift_min = shift
    elif shift == shift_min and ans > len(res):
        ans = len(res)

    s.appendleft(s.pop())
    n += 1

print(ans)